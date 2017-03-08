import codecs
from flask import render_template, send_from_directory

from showMe import app

from showMe.bin import services, tail

serviceHandler = services.Services


@app.route("/", methods=['POST', 'GET'])
def index():
    serviceHandler.add_service()
    return render_template("index.html")


@app.route("/log/<path:path>")
def logging(path):
    if path == 'Apache':
        logfile = '/var/log/apache2/error.log.1'
        f = codecs.open(logfile, "r", 'utf-8')
        # f = open(logfile, "r")
        log = tail.tail(f, 200, 4098)
        total_log = ""
        for line in log:
            # line += ' <br /> '
            total_log += line
        log = total_log.replace('\\n', ' <br /> ')
    else:
        log = 'No use able logfile.'
    return render_template("log.html", log=log)


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
