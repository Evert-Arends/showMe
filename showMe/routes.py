from flask import render_template, send_from_directory

from showMe import app
from showMe.bin import services

serviceHandler = services.Services


@app.route("/", methods=['POST', 'GET'])
def index():
    serviceHandler.add_service()
    return render_template("index.html")


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
