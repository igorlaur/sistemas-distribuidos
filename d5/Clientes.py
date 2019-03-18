clientes = []

def listar_todos():
    return clientes

def cadastrar_cliente(id, nome, email):
   novo_cliente = {"id": id, "nome": nome, "email": email}
   clientes.append(novo_cliente)


class ClienteNaoEncontradoException(Exception):
    pass

def pesquisar_cliente(id):
    for c in clientes:
        if c['id'] == id:
            return c
    raise ClienteNaoEncontradoException()

def excluir_cliente(id):
      c = pesquisar_cliente(id)
      clientes.remove(c)
