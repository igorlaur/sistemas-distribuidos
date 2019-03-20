# -*- coding: utf-8 -*-
from flask import flask
from flask import jsonify

app = Flask(__name__)

@app.route("ola/laur", methods = ["GET"])
def ola(nome):
    return {"Olá, " + nome}

if __name__ = "__main__":
    app.run(port = 5003, debug = True)
    pass
