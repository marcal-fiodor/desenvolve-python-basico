frase = input("Digite uma frase: ").lower()
palavra = input("Digite a palavra objetivo: ").lower()
tamanho = len(palavra)
anagramas = []

for i in range(len(frase) - tamanho + 1):
    trecho = frase[i:i+tamanho]
    if sorted(trecho) == sorted(palavra): 
        anagramas.append(trecho)

print("Anagramas encontrados:", anagramas)