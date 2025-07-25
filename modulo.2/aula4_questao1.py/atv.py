#Lê o comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno (em metros):"))
#Lê a largura do terreno
largura = int(input ("Digite a largura do terreno (em metros):"))
#Lê o preço do metro quadrado
preco_m2 = float(input("Digite o preço do m2 (em R$):"))
#calcula a area do terreno em m2
area_m2 = comprimento * largura
#calcula o preço total do terreno 
preco_total = preco_m2 * area_m2
## Exibe a área e o preço total do terreno
print (f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")