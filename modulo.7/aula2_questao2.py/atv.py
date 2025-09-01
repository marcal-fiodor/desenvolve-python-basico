vogais = "aeiouAEIOU"
frase_modificada = ""
frase = input("Digite uma frase: ")
for i in frase:
    if i in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += i
print(frase_modificada)
