genero = input ("Digite seu gênero(M para masculino e F para feminino): ").lower()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço(em anos): "))
regra_idade_m = genero == "m" and idade >= 65
regra_idade_f = genero == "f" and idade >= 60
regra_tempo = tempo_servico >= 30
regra_mista = idade >= 60 and tempo_servico >= 25
aposentar = regra_idade_m or regra_idade_f or regra_tempo or regra_mista
print(aposentar)
