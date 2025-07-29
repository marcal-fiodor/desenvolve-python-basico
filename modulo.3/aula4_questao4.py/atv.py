#Entrada de dados
distancia = int(input("Digite a distância em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

#Processamento
if distancia <= 100:
    frete = peso * 1
if distancia > 100 and distancia <= 300:
    frete = peso * 1.5
if distancia > 300:
    frete = peso * 2
#Taxa adicional 
if peso > 10:
    frete += 10
#Saída de dados
print(f"O valor do frete é: R$ {frete:.2f}")
