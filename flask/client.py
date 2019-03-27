# -*- coding: utf-8 -*-
import requests as Req

Url = "http://127.0.0.1/ola"
Dados = Req.api.get(Url).json()
print(Dados) 



