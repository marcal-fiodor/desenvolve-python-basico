#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

import random
n = random.randint(1,10)
resposta = int(input("Digite um valor de 1 a 10: "))

while resposta != n:

    if resposta > n:
        print("Muito alto. Tente de novo!")
    elif resposta < n:
        print("Muito baixo. Tente de novo!")

    resposta = int(input("Digite novamente: "))

print(f"Você acertou! O número é: {n}")