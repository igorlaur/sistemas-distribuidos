#!bin/python
from flask import Flask,jsonify,abort
from flask import request


app = Flask(__name__)


'''
Primeiramente, rode esse arquivo no cmd. Ele deve subir um
servidor.

Acesse a pagina http://localhost:5000/primeira/

Se deu tudo certo, deveria ter aparecido uma página com a string 
"funções matemáticas".
'''


'''
O comando seguinte define uma função index, que retorna 
a string "funções matemáticas".

Acima dele, podemos ver um decorator de python.

Esse decorator está associando a página /primeira/ a essa função
Quando você carrega a página no navegador, essa função roda
'''

@app.route('/primeira/')
def index():
        print('mama mia')
        return "Funcoes matematicas!"
'''
Voce pode ver, no cmd, que a cada vez que voce carrega a página, a string
"mama mia" aparece (no cmd)
'''

'''
A próxima função nos ensina a ler um pedaço da URL que foi passada

Por exemplo, ao acessarmos 
http://localhost:5000/matematica/potencia_de_dois/5
a variavel "expoente" da função recebe o valor 5.
Por isso, recebemos  { "resposta": 32 }
ao acessar a página

A propósito: as funções do flask tem que retornar strings.
Assim, não podemos retornar o dicionario {'resposta':32}

Usamos a funcao jsonify para converter o dicionário de pythom
em uma string, respeitando o formato json.
'''
@app.route('/matematica/potencia_de_dois/<int:expoente>')
def potencia_de_dois(expoente):
        return jsonify({"resposta":(2**expoente)})

'''
A proxima função é um pouco melhor.
Ela bate com dois tipos de url diferente

Uma sem o expoente e uma com.

Se o expoente não foi mandado, ela consegue reclamar.
'''

@app.route('/matematica/potencia_de_dois_melhor/')
@app.route('/matematica/potencia_de_dois_melhor/<int:expoente>')
def potencia_de_dois_melhor(expoente=None):
        if expoente == None :
                return jsonify({"erro":"sem expoente"}), 400
        return jsonify({"resposta":(2**expoente)})


''' Note que, quando o usuário cometeu um erro e nao mandou o
expoente, a funcao retornou 2 valores. O primeiro é a string
a ser mostrada na página. O segundo é um número, representado
o código de status http 400.

O codigo de status 400 representa erro de usuário
'''

'''
A proxima função recebe dois parametros na URL, na forma de
query strings. No caso, são dois números, a e b, que devem
ser somados

Ou seja,

http://localhost:5000/matematica/soma?b=13&a=12

Deverá retornar

{
    "soma": 25
}

Perceba que, no caso de uma query string, não foi necessário
escrever as posicoes das variaveis na url do decorator.

'''

@app.route('/matematica/soma')
def soma_url():
  a = request.args.get('a', None) #vai no dicionario args e faz get('a',None)
                                  #ou seja, se nao tiver a chave 'a'
                                  #no dicionario args, vem um None
  b = request.args.get('b', None)
  if a == None or b == None:
    return jsonify({'erro':'variável faltando'}), 400
  try:
    dicionario = {"soma": (int(a)+int(b))}
    return jsonify(dicionario)
  except ValueError :
    return jsonify({"erro":"variável não é INT"}), 400

'''
Podemos ver um pouco mais sobre query strings na URL abaixo:
https://en.wikipedia.org/wiki/Query_string
'''

'''
Outro método menos obvio de fazer a mesma coisa é
usando POST.

No GET acima, nós passamos duas váriaveis na URL

Agora, com o post, vamos passar essas mesmas duas variáveis
através de um "arquivo"

Para a URL /matematica/soma, com o método POST,
queremos o seguinte:

Que ela receba um json no corpo (body) do request,
e esse json deve definir dois numeros (a e b)

Ela deve retornar um json {resposta: v} onde v=a+b

Se o json nao contiver as chaves a ou b, ela deve retornar
um erro 400 (request mal formado) e um texto de erro
'''

@app.route('/matematica/soma', methods=['POST'])
def soma():
  if not request.json:
    return jsonify({'error': 'Format not json'}), 400
  varA = request.json.get("a", None)
  varB = request.json.get("b", None)
  if varA == None or varB == None :
    return jsonify({'erro':'faltando uma variável'}), 400
  return jsonify({'resposta':(varA+varB)})


'''
Exercicio

Crie uma função olá que recebe uma string nome e devolve
"olá <nome>".

Ela deve "atender" na url /ola/<nome>
'''

def ola(nome):
    pass

'''
Exercicio

Crie uma função ola2 que recebe duas strings nome1 e nome2 e devolve
"olá fulano e ciclano".

Ela deve "atender" na url /ola_upgrade?pessoa1=fulano,pessoa2=ciclano
Use as query strings, como no exemplo
'''

def ola2():
    pass

'''
Exercicio

Crie uma funcao ola3, que atende na url /ola_upgrade (também!)
mas agora via POST.

Ela deve receber a pessoa1 e a pessoa2 via json
'''
def ola3():
    pass

'''
A partir daqui nao tem mais nada pra fazer
'''
if __name__ == '__main__':
   app.run(debug=True,port=5000)