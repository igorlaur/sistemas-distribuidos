# -*- coding: utf-8 -*-
x = 1
lista = []
print('Digite 10 números.')
while x <= 10:
    n = int(input('Digite um número: [ %s ]: '%x))
    lista.append(n)
    x += 1

print('O maior valor é:',max(lista))
print('O menor valor é:',min(lista))
print('A soma total da lista é:',sum(lista))
print('A media dos valores é:',sum(lista)/ 10)
lista.sort()
print("Ordem crecente",lista)
lista.reverse()
print("Ordem descrecente",lista)

