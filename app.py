"""
[Aplicación básica del microframework Flask de Python]

Author: Fortinux
Date: [2023/11]
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/servicios")
def servicios():
    return render_template("base.html")


@app.route("/contacto")
def contacto():
    return render_template("base.html")


@app.route("/admin")
def admin():
    return render_template("base.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404