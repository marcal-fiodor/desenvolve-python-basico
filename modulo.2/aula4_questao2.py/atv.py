#Lê a temperatura em fahrenheit
f = int(input("Digite a temperatura em graus Fahrenheit:"))
#Converte fahrenheit em celsius
c = int((f - 32) * (5/9))
#imprime o resultado da operação
print (f"{f} graus Fahrenheit são {c} graus Celsius")