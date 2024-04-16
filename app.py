#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Peter Simeth's basic flask pretty youtube downloader (v1.3)
https://github.com/petersimeth/basic-flask-template
© MIT licensed, 2018-2023
"""
from flask import Flask, render_template

DEVELOPMENT_ENV = True

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/main")
def mainpage():
    return render_template('main.html')

@app.route("/success")
def tymessage():
    return "Good looks"

if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)
