import sqlite3 as sql
from flask import request


class Services:
    def __init__(self):
        print "\n"

    @staticmethod
    def connect_db():
        conn = sql.connect('showMe/db.sqlite')
        return conn

    @staticmethod
    def get_services():
        conn = Services.connect_db()

        cur = conn.cursor()
        cur.execute("SELECT * FROM logs")

        rows = cur.fetchall()
        return rows

    @staticmethod
    def add_service():
        if request.method == 'POST':
            new_title = request.form.get("title")
            new_icon = request.form.get("sel_icon")
            new_path = request.form.get("path")
            print new_icon, new_title, new_path

    @staticmethod
    def edit_service(title):
        if request.method == 'POST':
            edited_title = request.form.get("title")
            edited_icon = request.form.get("sel_icon")
            edited_path = request.form.get("path")
            print edited_icon, edited_title, edited_path, title

    @staticmethod
    def delete_service(title):
        print title
