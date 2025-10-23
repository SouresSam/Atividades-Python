import os
os.system ("cls")

lista = dict()#dicionário vazio
lista = {'nome': 'Pedro' , 'idade': 25}
print(lista['nome'])
print(lista['idade'])
print(lista ['nome'] , 'sua idade é', lista ['idade'], 'Anos')

lista = {'nome': 'Pedro', 'idade': 25}
lista['sexo'] = 'M'
print(lista)

lista = {'nome': 'Pedro', 'idade': 25}
del lista['idade']
print(lista)

