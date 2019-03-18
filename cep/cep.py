# -*- coding: utf-8 -*-

import requests as Req

cep = input("Entre com o CEP: ")
url = f"http://viacep.com.br/ws/{cep}/json"
retorno = Req.get(url).json()

logradouro = retorno['logradouro']
cidade = retorno['localidade']
estado = retorno['uf']
print(f"{logradouro} - {cidade} - {estado}")