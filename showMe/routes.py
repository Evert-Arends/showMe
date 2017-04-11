from flask import render_template, send_from_directory
from flask import request

from showMe import app
from showMe.bin import services
from showMe.controllers.models import logs

serviceHandler = services.Services


@app.route("/", methods=['POST', 'GET'])
def index():
    logs = serviceHandler.get_services()
    print logs
    if 'add_s' in request.form:
        serviceHandler.add_service()
    return render_template("index.html", logs=logs)


@app.route("/edit_service/<title>", methods=['POST', 'GET'])
def edit_service(title):
    serviceHandler.edit_service(title)
    return render_template("edit_service.html")


@app.route("/del_service/<title>", methods=['POST', 'GET'])
def del_service(title):
    serviceHandler.delete_service(title)
    return render_template("del_service.html")


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
