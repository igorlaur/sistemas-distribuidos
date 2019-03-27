# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/ola", methods = ["GET"])
def ResponderOla():
   Dados = {"Mensagem": "Hello World 2!"}
   Resposta = jsonify(Dados)
   return Resposta

if __name__ == "__main__":
   app.run(port = 5002, debug = True)