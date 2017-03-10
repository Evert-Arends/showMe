from flask import render_template, send_from_directory
from flask import request

from showMe import app
from showMe.bin import services

serviceHandler = services.Services


@app.route("/", methods=['POST', 'GET'])
def index():
    if 'add_s' in request.form:
        serviceHandler.add_service()
    return render_template("index.html")


@app.route("/log/<path:path>")
def logging(path):
    if path == 'Apache':
        logfile = open('/var/log/httpd/error_log', 'r')
        log = logfile.read()
        # log = 'tetthfdsfhdsdf'
    else:
        log = 'No usable logfile.'
    return render_template("log.html", log=log)


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
