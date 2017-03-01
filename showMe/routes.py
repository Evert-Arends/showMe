from flask import render_template, send_from_directory
from flask import request

from showMe import app
import settings


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        new_title = request.form.get("title")
        new_icon = request.form.get("sel_icon")
        print new_icon, new_title
    return render_template("index.html")


@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)


@app.route("/license/")
def view_license():
    return render_template("license.html")
