import os
os.system('cls')

filme = {'titulo': 'StarWars' , 'Ano': 1977 ,'Diretor': 'George Lucas'}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v, in filme.items():
    print(f'O {k} é {v}')



