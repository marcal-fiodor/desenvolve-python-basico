
def calcular_digito(cpf_parcial):
    tamanho = len(cpf_parcial) + 1
    multiplicadores = list(range(tamanho, 1, -1))
    
    soma = sum(int(cpf_parcial[i]) * multiplicadores[i] for i in range(len(cpf_parcial)))
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

cpf_numeros = cpf.replace(".", "").replace("-", "")

if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
    print("CPF Inválido")
else:
    cpf_base = cpf_numeros[:9]
    digito1 = calcular_digito(cpf_base)
    digito2 = calcular_digito(cpf_base + str(digito1))
    
    if cpf_numeros[-2:] == f"{digito1}{digito2}":
        print("Válido")
    else:
        print("Inválido")
