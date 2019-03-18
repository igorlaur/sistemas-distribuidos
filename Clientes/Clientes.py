clientes = []

def listar_todos():
    return clientes

def cadastrar_cliente(id, nome, email):
    novo_cliente = {"id": id, "nome": nome, "email": email}
    clientes.append(novo_cliente) 

class ClienteNaoENcontradoException(Exception):
    pass

def pesquisar_cliente(id):
    for c in lista:
        if(c['id']) == id:
            return c
        raise ClienteNaoENcontradoException()
def seguir_clientes(id):
    c = pesquisar_cliente(id)
    lista.remove(c)