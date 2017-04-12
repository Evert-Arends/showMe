from flask import render_template, send_from_directory
from flask import request

from showMe import app
from showMe.bin import services
from showMe.controllers.models import logs

serviceHandler = services.Services


@app.route("/", methods=['POST', 'GET'])
def index():
    logs_to_page = serviceHandler.get_services()
    print logs_to_page
    if 'add_s' in request.form:
        response = serviceHandler.add_service()
        if response:
            logs_to_page = serviceHandler.get_services()
    return render_template("index.html", logs=logs_to_page)


@app.route("/edit_service/<path:path>", methods=['POST', 'GET'])
def edit_service(path):
    serviceHandler.edit_service(path)
    return render_template("edit_service.html")


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
        log = "No logs file found."
    else:
        open_file = logs.query.filter_by(name=path)
        logfile = open(open_file[0].path, 'r')
        log = logfile.read()
    return render_template("log.html", log=log)


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
