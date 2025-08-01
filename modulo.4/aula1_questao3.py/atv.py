#Entrada
n1 = int(input("Digite o vealor de n1: "))
n2 = int(input("Digite o vealor de n2: "))
n3 = int(input("Digite o vealor de n3: "))

#Processamento
m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")
#Saída
print("Fim")