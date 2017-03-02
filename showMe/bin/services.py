from flask import request


class Services:
    def __init__(self):
        print "\n"

    @staticmethod
    def add_service():
        if request.method == 'POST':
            new_title = request.form.get("title")
            new_icon = request.form.get("sel_icon")
            print new_icon, new_title
