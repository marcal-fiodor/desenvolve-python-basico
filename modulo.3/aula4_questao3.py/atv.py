#Entrada de dados 
ano = int(input("Digite um ano: "))

#Processamento 
ano_bissexto = ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0

#Saída de dados
if ano_bissexto:
    print("O ano digitado é bissexto!")
else:
    print("O ano digitado não é bissexto.")