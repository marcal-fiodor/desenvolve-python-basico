#Produto 1
nome1= input("Digite o nome do produto 1")
preco1= float(input("Digite o preço unitário do produto 1:"))
quantidade1= int (input("Digite a quantidade do produto 1:"))
#Produto 2
nome2= input("Digite o nome do produto 2")
preco2= float(input("Digite o preço unitário do produto 2:"))
quantidade2= int (input("Digite a quantidade do produto 2:"))
#Produto 3
nome3= input("Digite o nome do produto 3")
preco3= float(input("Digite o preço unitário do produto 3:"))
quantidade3= int (input("Digite a quantidade do produto 3:"))

#total
total = (quantidade1 * preco1) + (quantidade2 * preco2) + (quantidade3 * preco3)
print (f"Total: R${total:,.2f}")