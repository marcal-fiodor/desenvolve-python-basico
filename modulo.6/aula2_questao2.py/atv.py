import random
valores = []
elementos = []
num_elementos = random.randint(5, 20)
for i in range(num_elementos):
    valores = random.randint(1, 10)
    elementos.append(valores)
print("Lista dos elementos: ",elementos)
print("Soma dos valores da lista: ",sum(elementos))
print("Média dos valores da lista: ",(sum(elementos)) / (len(elementos)))