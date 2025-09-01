meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = data.split("/")


mes_extenso = meses[int(mes) - 1]


print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
