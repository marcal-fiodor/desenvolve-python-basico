import random

def encrypt(nomes):
    chave = 5  
    nomes_cript = []

    for nome in nomes:
        cript = ""
        for c in nome:
            novo = (ord(c) - 33 + chave) % (126 - 33 + 1) + 33
            cript += chr(novo)
        nomes_cript.append(cript)

    return nomes_cript, chave


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomes_cript, chave_aleatoria = encrypt(nomes)


print("Nomes originais:", nomes)
print("Chave usada:", chave_aleatoria)
print("Nomes criptografados:", nomes_cript)

print("Detalhado:")
for original, cript in zip(nomes, nomes_cript):
    print(f"{original}  →  {cript}")
