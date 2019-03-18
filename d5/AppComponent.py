from Clientes import *

cadastrar_cliente(1, "Pedro", "pedro@gmail.com")
cadastrar_cliente(2, "Maria", "maria@gmail.com")
cadastrar_cliente(3, "Jose", "jose@gmail.com")

excluir_cliente(2)

for c in listar_todos():
    print(str(c['id']) + "/" + c['nome'] + "/" + c["email"])

try:
    pesquisar_cliente(6)
except ClienteNaoEncontradoException as x:
    print('Não encontrado')

