n = int(input("Digite quantas pessoas serão entrevistadas: "))

#Processamento
soma = 0
cont = 0
while cont < n:
    idade = int(input("Digite as idades: "))
    soma += idade
    cont += 1
#Saída
print(soma)
print(f"A média das idades é {soma/n:.0f} anos.")