import random

valores = []
for i in range(20):
    num_inteiro = random.randint(-100, 100)
    valores.append(num_inteiro)

maior_valor = max(valores)
indice_maior = valores.index(maior_valor)

menor_valor = min(valores)
indice_menor = valores.index(menor_valor)

print(sorted(valores))
print(valores)
print(indice_maior)
print(indice_menor)

