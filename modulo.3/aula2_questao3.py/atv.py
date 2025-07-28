idade = int(input("Digite sua idade: "))
qtd_jogos = input("Você já jogou ao menos 3 jogos de tabuleiro? Responda true para sim, e false para não: ")
vitorias = int(input("Quantas vezes você já venceu um jogo? "))
print(16<= idade <=18 and qtd_jogos.lower() == "true" and vitorias > 0)