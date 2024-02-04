from flask import Flask, session, jsonify, render_template, redirect, url_for, request as flask_request
import http.client
import sqlite3
import json
import os

DB_FILE = "task_tracker.db"
db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tasks(title TEXT, priority TEXT, date TEXT, hours TEXT)''')

def import_tasks(stored_data):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("insert into tasks values (?,?,?,?);", stored_data)
    db.commit()
    db.close()

def get_all_tasks():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    usertask = c.execute("SELECT title from tasks;").fetchall()
    db.commit()
    db.close()
    return usertask

def get_priority(title):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT priority FROM tasks where title=?", (title,))
    priority_lvl = c.fetchone()
    db.commit()
    db.close()
    return priority_lvl[0]

def get_date(title):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT date FROM tasks where title=?", (title,))
    all_dates = c.fetchone()
    db.commit()
    db.close()
    return all_dates[0]

def get_hours(title):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT hours FROM tasks where title=?", (title,))
    hours_time = c.fetchone()
    db.commit()
    db.close()
    return hours_time[0]