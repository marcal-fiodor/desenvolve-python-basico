import random
lista1, lista2 = [], []
interseccao = []
for i in range(10):
    numeros1 = random.randint(0, 50)
    numeros2 = random.randint(0,50)
    lista1.append(numeros1)
    lista2.append(numeros2)
interseccao = list(set(lista1) & set(lista2))
print("Elementos lista 1: ",lista1)
print("Elementos lista 2: ",lista2)
print("Interseção ordenada:", sorted(interseccao))

print("Contagem dos elementos da interseção:")
for elemento in sorted(interseccao):
    qtd_lista1 = lista1.count(elemento)
    qtd_lista2 = lista2.count(elemento)
    print(f"Elemento {elemento}: Lista1 = {qtd_lista1}, Lista2 = {qtd_lista2}")
