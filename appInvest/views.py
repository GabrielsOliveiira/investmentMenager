from appInvest import app
from flask import render_template, url_for

@app.route("/")
def homepage():
    usuario = "ca"
    idade = 16
    context = {
        "usuario": usuario,
        "idade": idade
    }
    return render_template('index.html', context=context)

@app.route("/login/")
def login():
    return "render_template('index.html')"