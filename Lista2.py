compras=['arroz','feijão','alho','ovo','leite']
print(compras [1])

print("="*35)

print(compras [0:2])

print("="*35)

print(len(compras [1]))

print("="*35)

compras=['arroz','feijão','alho','ovo','leite']

compras[3]="frango"
compras[1]="feijoada"
print(compras)

print("="*35)

compras=['arroz','feijão','alho','ovo','leite']

compras.append("café")
print(compras)

print("="*35)

compras=['arroz','feijão','alho','ovo','leite']

compras.insert(2,"pão")
print(compras)

print("="*35)

compras=['arroz','feijão','alho','ovo','leite']

del compras[3]
compras.pop(1)
compras.remove('leite')
print(compras)

print("="*35)

compras=['arroz','feijão','alho','ovo','leite','chocolate']

if "chocolate" in compras:
    compras.remove("chocolate")
    print(compras)

print("="*35)

valores=list(range(4,16))
print(valores)

print("="*35)

numeros=[1,4,5,8,7,9,4,6,3]
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

print("="*35)

#val=list()
val=[]

val.append(5)
val.append(9)
val.append(6)
print(val)

for v in val:
    print(f"{v}...")
    print(f"{v}...",end='')


for c, v in enumerate (val ):
    print(f"na posição {c+1} enocntrei o valor {v}!")
    print ("cheguei ao final da lista")



