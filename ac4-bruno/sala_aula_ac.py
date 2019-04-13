################################ EXERCICIO #####################################
#   Criar um arquivo sala_aula_ac.py.
#   Criar uma função rotas REST para aluno e professor. Possíveis ROTAS:
#   1. Retrieve (consulta por ID)
#   2. Lista (consulta geral)
#   3. Create (inserir)
#   4. Delete (remover) **
#   5. Update (atualizar) ***
################################ GRUPO #########################################
#   Abraao Ylgner da Rocha Silva - 1600301
#   Bruno Borges Furukawa - 1601320
#   Diego João Gallego - 1601084
#   Igor Gusmão Laur - 1601230
#   Leonardo Laurino Serinhano - 1600925
#   Lincoln Morais de Melo - 1601212
################################################################################

# instalar o modulo FLASK -> pip install flask

from flask import Flask, jsonify, request

app = Flask(__name__)

database = dict()
database['ALUNO'] = []
database['PROFESSOR'] = []

# insere um novo aluno pelo metodo POST
@app.route('/alunos', methods = ['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    print("inserindo: " + str(novo_aluno))
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

# insere um novo professor pelo metodo POST
@app.route('/professores', methods = ['POST'])
def novo_professor():
    novo_professor = request.get_json()
    print("inserindo: " + str(novo_professor))
    database['PROFESSOR'].append(novo_professor)
    return jsonify(database['PROFESSOR'])

# lista todo o dicionario
@app.route('/')
def all():
    return jsonify(database)

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

# pega aluno por ID
@app.route('/alunos/<int:id_aluno>', methods = ['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return '', 404

# remove aluno por ID
@app.route('/alunos/remove/<int:id_aluno>', methods = ['GET'])
def remove_aluno(id_aluno):
    index = 0
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            del database['ALUNO'][index]
            return jsonify(aluno)
        index = index + 1
    return '', 404

# atualiza aluno por ID
@app.route('/alunos/update/<int:id_aluno>', methods=['PUT'])
def atualiza_aluno(id_aluno):
    novo_aluno = request.get_json()
    index = 0
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            del database['ALUNO'][index]
            database['ALUNO'].append(novo_aluno)
            return jsonify(novo_aluno)
        index = index + 1
    return '', 404

# pega professor por ID
@app.route('/professores/<int:id_professor>', methods = ['GET'])
def localiza_professor(id_professor):
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            return jsonify(professor)
    return '', 404

# remove professor por ID
@app.route('/professores/remove/<int:id_professor>', methods = ['GET'])
def remove_professor(id_professor):
    index = 0
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            del database['PROFESSOR'][index]
            return jsonify(professor)
        index = index + 1
    return '', 404

# atualiza professor por ID
@app.route('/professores/update/<int:id_professor>', methods=['PUT'])
def atualiza_professor(id_professor):
    novo_professor = request.get_json()
    index = 0
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            del database['PROFESSOR'][index]
            database['PROFESSOR'].append(novo_professor)
            return jsonify(novo_professor)
        index = index + 1
    return '', 404

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)