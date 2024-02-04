from flask import Flask, jsonify, render_template, session, request, redirect, url_for, abort
from datetime import datetime
from createjson import *
import os.path
import task_tracker

# from events import eventsToAdd
# from datetime import datetime
from datetime import timedelta
from datetime import timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# front-end to tell server to run function 
# front-end will prob do fetch (API)

app = Flask(__name__)

# return error 404 for good practice
# @app.route('/')
# def home():
#    return 404

@app.route('/add_tasks', methods=['POST'])
def add_tasks():
    tasks = request.form.getlist['allSubmissions']
    task_list = []

    for task_data in tasks:
        title = task_data.get('title')
        priority_str = task_data.get('priority')
        date_str = task_data.get('date')
        hours = task_data.get('hours')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        # Create a dictionary for each task
        task_dict = {'title': title, 'priority': priority_str, 'date': date, 'hours': hours}
        task_list.append(task_dict)

    # Call import_tasks with the list of tasks
    import_tasks(task_list)

    return "Tasks added successfully"

@app.route('/scheduling_tasks', methods=['POST'])
def scheduling_tasks():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  
  timeZone = "US/Eastern"
  today = datetime.datetime.today()
  tomorrowStart = today + timedelta(days = 1)
  dayStart = datetime.datetime(tomorrowStart.year, tomorrowStart.month, tomorrowStart.day, 00, 00).isoformat() + "Z"
  tomorrowEnd = tomorrowStart + datetime.timedelta(days=1)
  dayEnd = datetime.datetime(tomorrowEnd.year, tomorrowEnd.month, tomorrowEnd.day, 5, 00).isoformat() + "Z"
  taskStartChange = datetime.timedelta(hours = 9)
  taskEndChange = datetime.timedelta(hours = 22)
  taskStart = tomorrowStart + taskStartChange
  taskEnd = tomorrowEnd + taskEndChange

  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    events_result = (
      service.events()
      .list(
        calendarId="primary", 
        timeMin=dayStart, 
        timeMax=dayEnd, 
        singleEvents=True, 
        orderBy="startTime",
        )
      .execute()
    )

    print(dayStart)
    print(dayEnd)
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    # for event in events:
    #   start = event["start"].get("dateTime", event["start"].get("date"))
    #   print(start, event["summary"])

    taskIndex = 0;

    tz_offset = timedelta(hours=-5)

    i = 0
    while (i < len(events) - 1):
      start = events[i].get("dateTime", events[i]["start"].get("date"))
      print(taskIndex)
      print(start, events[i]["summary"])
      prevEnd = datetime.datetime.strptime(events[i]["end"].get("dateTime", events[i + 1]["end"].get("date")), "%Y-%m-%dT%H:%M:%S%z")
      currStart = datetime.datetime.strptime(events[i + 1]["start"].get("dateTime", events[i]["start"].get("date")), "%Y-%m-%dT%H:%M:%S%z")
      prevEndWithTZ = prevEnd.replace(tzinfo=timezone(tz_offset))
      if currStart - prevEnd >= datetime.timedelta(hours = 1):
        if (currStart - prevEnd > datetime.timedelta(hours = tasks[taskIndex]["hours"])):
          currTaskEnd = prevEndWithTZ +  timedelta(hours = tasks[taskIndex]["hours"])
          event = {
            "summary": task_tracker[taskIndex].get("name"),
            "start": {
              "dateTime": events[i]["end"].get("dateTime", events[i]["end"].get("date")),
              "timeZone": timeZone
            },
            "end": {
              "dateTime": currTaskEnd.strftime("%Y-%m-%dT%H:%M:%S%z"),
              "timeZone": timeZone
            }
          }
          event = service.events().insert(calendarId = "primary", body = event).execute()
          task_tracker[taskIndex]["hours"] = 0
          taskIndex += 1
          events.insert(i + 1, event)
        else:
          currTaskEnd = prevEndWithTZ + timedelta(hours = (currStart - prevEnd).seconds//3600)
          event = {
            "summary": tasks[taskIndex].get("name"),
            "start": {
              "dateTime": events[i]["end"].get("dateTime", events[i]["end"].get("date")),
              "timeZone": timeZone
            },
            "end": {
              "dateTime": currTaskEnd.strftime("%Y-%m-%dT%H:%M:%S%z"),
              "timeZone": timeZone
            }
          }
          event = service.events().insert(calendarId = "primary", body = event).execute()
          task_tracker[taskIndex]["hours"] = task_tracker[taskIndex]["hours"] - (currStart - prevEnd).seconds//3600
          # events.insert(i, event)
        # events = events_result.get("items", [])
        # i -= 1
      i += 1

  except HttpError as error:
    print(f"An error occurred: {error}")

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run(host = '0.0.0.0', port=80)