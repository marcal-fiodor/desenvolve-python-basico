import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = palavra[0] + "".join(meio) + palavra[-1]
            resultado.append(nova_palavra)
        else:
            resultado.append(palavra)

    return " ".join(resultado)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
