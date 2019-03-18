from Clientes import listar_todos, cadastrar_cliente

cadastrar_cliente(1, "Pedro", "pedro@gmail.com")
cadastrar_cliente(2, "Maria", "maria@gmail.com")
cadastrar_cliente(3, "Jose", "jose@gmail.com")

for c in listar_todos():
    print(str(c['id']) + " - " + c['nome']);