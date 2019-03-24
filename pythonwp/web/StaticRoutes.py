from pythonwp import app
from flask import render_template, request, send_from_directory

@app.route('/')
def getRoot():
    return send_from_directory("static", "index.html")

@app.route("/js/<path:path>")
def getJs(path):
    return send_from_directory("static/js", path)

@app.route("/css/<path:path>")
def getCss(path):
    return send_from_directory("static/css", path)

@app.route("/partials/<path:path>")
def getPartials(path):
    return send_from_directory("static/partials", path)

@app.route("/img/<path:path>")
def getImg(path):
    return send_from_directory("static/img", path)
