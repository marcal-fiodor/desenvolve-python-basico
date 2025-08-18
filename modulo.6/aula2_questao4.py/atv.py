qnd_elementos_lista1 = int(input("Digite a quantidade de elementos na lista 1: "))
elementos_lista1 = []
for i in range(qnd_elementos_lista1):
    elementos1 = int(input(f"Digite os {qnd_elementos_lista1} elementos da lista 1: "))
    elementos_lista1.append(elementos1)

qnd_elementos_lista2 = int(input("Digite a quantidade de elementos na lista 2: "))
elementos_lista2 = []
for i in range(qnd_elementos_lista2):
    elementos2 = int(input(f"Digite os {qnd_elementos_lista2} elementos da lista 2: "))
    elementos_lista2.append(elementos2)


lista_intercalada = []
tamanho_min = min(len(elementos_lista1), len(elementos_lista2))

for i in range(tamanho_min):
    lista_intercalada.append(elementos_lista1[i])
    lista_intercalada.append(elementos_lista2[i])

if len(elementos_lista1) > len(elementos_lista2):
    lista_intercalada.extend(elementos_lista1[tamanho_min:])
else:
    lista_intercalada.extend(elementos_lista2[tamanho_min:])


print("Lista 1:", elementos_lista1)
print("Lista 2:", elementos_lista2)
print("Lista intercalada", lista_intercalada)