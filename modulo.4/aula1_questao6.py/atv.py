#Entrada de cobaias
n_experimentos = int(input("Digite a quantidade de experimentos registrados: "))

#Processamento de dados
total_cobaias = 0
soma_sapo = 0
soma_rato = 0
soma_coelho = 0
cont = 0
while cont < n_experimentos:
    cobaias = int(input("Digite o número de cada cobaia utilizada: "))
    tipo_cobaia = input("Digite o tipo de cobaia utilizada (S, R ou C): ").lower()
    total_cobaias += cobaias

    if tipo_cobaia == "s":
        soma_sapo += cobaias
    elif tipo_cobaia == "r":
        soma_rato += cobaias
    elif tipo_cobaia == "c":
        soma_coelho += cobaias

    cont += 1
#Saída
percentual_sapo = (soma_sapo / total_cobaias) * 100
percentual_rato = (soma_rato / total_cobaias) * 100
percentual_coelho = (soma_coelho / total_cobaias) * 100

print("O total de cobaias utilizadas é: ", total_cobaias)
print("O total de sapos utilizados foi: ", soma_sapo)
print("O total de ratos utilizados foi: ", soma_rato)
print("O total de coelhos utilizados foi: ", soma_coelho)

print(f"O percentual de sapos utilizados é: {percentual_sapo:.2f} %")
print(f"O percentual de ratos utilizados é: {percentual_rato:.2f} %")
print(f"O percentual de coelhos utilizados é: {percentual_coelho:.2f} %")