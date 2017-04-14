from flask import render_template, send_from_directory
from flask import request

from showMe import app
from showMe.bin import services, tail
from showMe.controllers.models import logs

serviceHandler = services.Services
fileTail = tail.TailLog


@app.route("/", methods=['POST', 'GET'])
def index():
    logs_to_page = serviceHandler.get_services()
    if 'add_s' in request.form:
        response = serviceHandler.add_service()
        if response:
            logs_to_page = serviceHandler.get_services()
    return render_template("index.html", logs=logs_to_page)


@app.route("/edit_service/<path:path>", methods=['POST', 'GET'])
def edit_service(path):
    called = serviceHandler.get_called(path)
    update = ""
    if 'edit_s' in request.form:
        update = serviceHandler.edit_service(path)
        if update:
            update = True
        else:
            update = False
    return render_template("edit_service.html", called=called, update=update)


@app.route("/del_service/<path:path>", methods=['POST', 'GET'])
def del_service(path):
    response = ""
    if 'del_s' in request.form:
        delete = serviceHandler.delete_service(path)
        if delete:
            response = True
        else:
            response = False
    return render_template("del_service.html", response=response)


@app.route("/log/<path:path>")
def logging(path):
    if path == '':
        log_content = "No logs file found."
    else:
        open_file = logs.query.filter_by(name=path)
        logfile = open(open_file[0].path, 'r')
        log_content = fileTail.tail(logfile, 100, 4098)
    return render_template("log.html", log=log_content)


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
