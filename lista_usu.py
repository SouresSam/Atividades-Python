'''lista_usu= list()
for cont in range (0,5):
    lista_usu.append(int(input("digite um valor:")))
for c, v in enumerate(lista_usu):
    print (f"na posição {c+1} encontrei o valor {v}!")
print('cheguei ao final da lista')'''


a=[2,4,5]
b=a[:] 

b[2]=8

print(f'lista A = {a}')
print(f'lista B = {b}')
