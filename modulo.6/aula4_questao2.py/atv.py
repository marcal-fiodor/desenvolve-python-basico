frase = input("Digite uma frase: ")

vogais = sorted([letra for letra in frase if letra.lower() in "aeiou"])
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() in "bcdfghjklmnpqrstvwxyz"]

print("Vogais:", vogais)
print("Consoantes:", consoantes)
