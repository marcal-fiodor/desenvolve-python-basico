import random
import math

n = int(input("Digite a quantidade de números aleatórios: "))
soma = 0

for i in range(n):
    valor = random.randint(0, 100)
    soma += valor
    print(f"Valor gerado #{i+1}: {valor}")

raiz = math.sqrt(soma)
print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz:.2f}")


