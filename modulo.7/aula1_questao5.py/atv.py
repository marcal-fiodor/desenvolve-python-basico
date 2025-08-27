frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
indices = []

for i, letra in enumerate(frase):
    if letra in vogais:
        indices.append(i)

print(f"Quantidade de vogais: {len(indices)}")
print(f"Índices das vogais: {indices}")

