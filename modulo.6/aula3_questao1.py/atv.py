numeros = []

print("Digite números inteiros (digite 0 para parar)")
while True:
    valor = int(input("Número: "))
    if valor == 0:
        if len(numeros) >= 4:  # só deixa parar se já tiver pelo menos 4 valores
            break
        else:
            print("Digite pelo menos 4 números antes de encerrar")
    else:
        numeros.append(valor)

print("Lista original: ", numeros[::])
print("3 primeiros elementos:", numeros[0:3])
print("2 últimos elementos:", numeros[-1:-3:-1])
print("Lista invertida:", numeros[::-1])
print("Elementos índice par:", numeros[::2])
print("Elementos indíce ímpar:", numeros[1::2])