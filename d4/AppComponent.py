 from Clientes import listar_todos, cadastrar_cliente

cadastrar_cliente(1, "Pedro", "pedro@gmail.com")
cadastrar_cliente(2, "Maria", "maria@gmail.com")
cadastrar_cliente(3, "Jose", "jose@gmail.com")
cadastrar_cliente(4, "Alvaro", "alvaro@gmail.com")

for c in listar_todos():
    print(str(c['id']) + "/" + c['nome'] + "/" + c["email"])

class Exemplo:
    def __init__(self):
        pass

    def hello(self):
        print("Hello")

    def __str__(self):
        return "jjjj"

a = Exemplo()
print(Exemplo)
