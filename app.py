from flask import Flask, render_template

app = Flask("__name__")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/quem-somos.html")
def quemsomos():
    return render_template("quem-somos.html")

@app.route("/contatos.html")
def contatos():
     return render_template("contatos.html")