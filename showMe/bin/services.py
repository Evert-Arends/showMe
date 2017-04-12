from flask import request

from showMe import db
from showMe.controllers.models import logs
from sqlalchemy import exc

class Services:
    def __init__(self):
        print "\n"

    @staticmethod
    def get_services():
        rows = logs.query.all()
        return rows

    @staticmethod
    def add_service():
        if request.method == 'POST':
            new_title = request.form.get("title")
            new_icon = request.form.get("sel_icon")
            new_path = request.form.get("path")
            print new_icon
            insert = logs(new_title, new_icon, new_path)
            db.session.add(insert)
            db.session.commit()
        return True

    @staticmethod
    def edit_service(title):
        if request.method == 'POST':
            edited_title = request.form.get("title")
            edited_icon = request.form.get("sel_icon")
            edited_path = request.form.get("path")
            print edited_icon, edited_title, edited_path, title

    @staticmethod
    def delete_service(path):
        try:
            log_to_delete = logs.query.filter_by(name=path).first()
            db.session.delete(log_to_delete)
            db.session.commit()
            return True
        except exc.SQLAlchemyError:
            return False
