import codecs

from flask import render_template, send_from_directory
from flask import request

from showMe import app

from showMe.bin import services, tail


serviceHandler = services.Services


@app.route("/", methods=['POST', 'GET'])
def index():
    if 'add_s' in request.form:
        serviceHandler.add_service()
    return render_template("index.html")


@app.route("/edit_service/", methods=['POST', 'GET'])
def edit_service():
    serviceHandler.edit_service()
    return render_template("edit_server.html")


@app.route("/del_service/<title>", methods=['POST', 'GET'])
def del_service(title):
    serviceHandler.delete_service(title)
    return render_template("del_service.html")


@app.route("/log/<path:path>")
def logging(path):
    if path == 'Apache':
        logfile = '/var/log/httpd/error_log'
        f = codecs.open(logfile, "r", 'utf-8')
        # f = open(logfile, "r")
        log = tail.tail(f, 200, 4098)
        total_log = ""
        for line in log:
            total_log += line
        log = total_log.replace('\\n', ' <br /> ')

    if path == 'Mysql':
        logfile = '/var/log/httpd/error_log'
        f = codecs.open(logfile, "r", 'utf-8')
        # f = open(logfile, "r")
        log = tail.tail(f, 200, 4098)
        total_log = ""
        for line in log:
            total_log += line
        log = total_log.replace('\\n', ' <br /> ')
    else:
        log = 'No usable logfile.'
    return render_template("log.html", log=log)


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
