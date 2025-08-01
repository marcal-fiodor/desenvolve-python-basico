#Entrada
n = int(input("Digite o valor de n:" ))

#Processamento
maior = 0
while n > 0:
    x = int(input("Digite o valor de x: "))
    if x > maior:
        maior = x
    n = n - 1
#Saída
print(maior)