import os
os.system('cls')

'''Brasil = []
Estado = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
Estado2 = {'uf':'São Paulo', 'sigla':'SP'}
Brasil.append(Estado)
Brasil.append(Estado2)
print(Brasil)
print(Brasil[0])
print(Brasil[1])
print(Brasil[0]['sigla'])
print(Brasil[1]['uf'])'''



'''materia = dict()
curso=list()
for c in range (0,3):
    materia['sigla'] = str(input('Digite a sigla da matéria:'))
    materia['nome'] = str(input('Digite o nome da matéria:'))
    curso.append(materia.copy()) #para copiar a lista e torna independente 
print(curso)

for m in curso:
    for k, v, in m.items():
        print({f"o campo {k} tem valor {v}"}) '''

lista = []
dic=dict()

nome=str(input("digite seu nome:"))
idade=int(input("digite sua idade: "))

lista.append(nome)
lista.append(idade)

dic={"nome": lista[0], "idade":lista[1]}

print(lista)
print(dic['nome'])

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979 },
    'Jetta': {'km': 56000, 'ano': 2011 },
    'Passart': {'km': 62000, 'ano': 1999 },
}

for item in dados.items():
    print(item)
for item in dados.items():
    print(item[1]['ano'])





