from flask import render_template, send_from_directory
from flask import request
from controllers import services
from showMe import app

addService = services.Services


@app.route("/", methods=['POST', 'GET'])
def index():
    addService.add_service()
    return render_template("index.html")


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
