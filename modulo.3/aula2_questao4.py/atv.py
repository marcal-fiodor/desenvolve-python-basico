classe = input("Escolha uma classe de personagem(Guerreiro, Mago ou Arqueiro): ").lower()
forca = int(input("Quantos pontos de força? (De 1 a 20): "))
magia = int(input("Quantos pontos de magia? (De 1 a 20): "))
valido = ( (classe == "guerreiro" and forca >=15 and magia <= 10) or
(classe == "mago" and forca <= 10 and magia >= 15) or
(classe == "arqueiro" and 5 <= forca <= 15 and 5<= magia <=15 )  )
print("Pontos de atributo consistentes com a classe escolhida:", valido)