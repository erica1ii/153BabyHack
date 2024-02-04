import datetime
import os.path

timeZone = "US/Eastern"

tasks = [
  {
    "name": "CS HW 1c",
    "due": datetime.datetime(2024, 2, 8),
    "priority": 3,
    "hours": 2,
  },
  {
    "name": "LINALG",
    "due": datetime.datetime(2024, 2, 9),
    "priority": 2,
    "hours": 1,
  },
  {
    "due": datetime.datetime(2024, 2, 8),
    "priority": 2
  }
]

sort1 = sorted(tasks, key=lambda x: x["due"])
sort2 = sorted(tasks, key=lambda x: x["priority"])
for task in sort2:
  print(task)



# eventsToAdd = [
#   {
#     "summary": "event 1",
#     "start": {
#       "dateTime": "2024-02-03T20:00:00-05:00",
#       "timeZone": timeZone,
#     },
#     "end": {
#       "dateTime": "2024-02-03T22:00:00-05:00",
#       "timeZone": timeZone,
#     }
#   },
#   {
#     "summary": "event 2",
#     "start": {
#       "dateTime": "2024-02-03T18:00:00-05:00",
#       "timeZone": timeZone,
#     },
#     "end": {
#       "dateTime": "2024-02-03T20:00:00-05:00",
#       "timeZone": timeZone,
#     }
#   }
# ]