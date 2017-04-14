from flask import request

from showMe import db
from showMe.controllers.models import logs
from sqlalchemy import exc


class Services:
    def __init__(self):
        print "\n"

    @staticmethod
    def get_services():
        try:
            rows = logs.query.all()
            return rows
        except exc.SQLAlchemyError:
            return False

    @staticmethod
    def get_called(path):
        try:
            called = logs.query.filter_by(name=path)
            return called
        except exc.SQLAlchemyError:
            return False

    @staticmethod
    def add_service():
        if request.method == 'POST':
            try:
                new_title = request.form.get("title")
                new_icon = request.form.get("sel_icon")
                new_path = request.form.get("path")
                insert = logs(new_title, new_icon, new_path)
                db.session.add(insert)
                db.session.commit()
                return True
            except exc.SQLAlchemyError:
                return False

    @staticmethod
    def edit_service(path):
        try:
            edited_title = request.form.get("title")
            edited_icon = request.form.get("sel_icon")
            edited_path = request.form.get("path")
            update = logs.query.filter_by(name=path).first()
            update.name = edited_title
            update.icon = edited_icon
            update.path = edited_path
            db.session.commit()
            return True
        except exc.SQLAlchemyError:
            return False

    @staticmethod
    def delete_service(path):
        try:
            log_to_delete = logs.query.filter_by(name=path).first()
            db.session.delete(log_to_delete)
            db.session.commit()
            return True
        except exc.SQLAlchemyError:
            return False
