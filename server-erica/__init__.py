from flask import Flask, jsonify, render_template, session, request, redirect, url_for, abort
from datetime import datetime
from createjson import *

# front-end to tell server to run function 
# front-end will prob do fetch (API)

app = Flask(__name__)

# return error 404 for good practice
# @app.route('/')
# def home():
#    return 404

@app.route('/update_tasks', methods=['POST'])
def update_tasks():
    # Get the form data
    title = request.form.get('title')
    priority_str = request.form.get('priority')
    date_str = request.form.get('date')
    hours = request.form.get('hours')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    data = [title, priority_str, date, hours]
    import_tasks(data)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run(host = '0.0.0.0', port=80)