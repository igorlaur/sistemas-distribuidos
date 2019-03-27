from flask import Flask, jsonify, request

app = Flask(__name__)

database = dict()
database['ALUNO'] = []
database['PROFESSOR'] = []

@app.route('/alunos', methods = ['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

@app.route('/')
def all():
    return jsonify(database)

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/alunos/<int:id_aluno>', methods = ['GET'])

if __name__ == '__main__':
    app.run()
