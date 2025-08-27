numero = input("Digite o número de celular: ")
if len(numero) == 8:
    numero = "9" + numero

elif len(numero) == 9:
    if numero[0] != "9":
        print("Número inválido: celular com 9 dígitos deve começar com 9")
    else:
        print("Número já está correto")
else:
    print("Número inválido: deve ter 8 ou 9 dígitos")


if len(numero) == 9 and numero[0] == "9":
    numero_formatado = numero[:5] + "-" + numero[5:]
    print("Número formatado:", numero_formatado)
