clientes = []

def listar_todos():
    return clientes

def cadastrar_cliente(id, nome, email):
   novo_cliente = {"id": id, "nome": nome, "email": email}
   clientes.append(novo_cliente)
