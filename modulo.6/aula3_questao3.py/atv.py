import random
numero = []
for i in range(20):
    nums = random.randint(-10, 10)
    numero.append(nums)
print("Lista original:", numero)

max_inicio, max_fim, max_tamanho = 0, 0, 0
inicio = None

for i, n in enumerate(numero):
    if n < 0:
        if inicio is None:   
            inicio = i
    else:
        if inicio is not None:  
            tamanho = i - inicio
            if tamanho > max_tamanho:
                max_tamanho = tamanho
                max_inicio, max_fim = inicio, i
            inicio = None

if inicio is not None:
    tamanho = len(numero) - inicio
    if tamanho > max_tamanho:
        max_tamanho = tamanho
        max_inicio, max_fim = inicio, len(numero)

if max_tamanho > 0:
    del numero[max_inicio:max_fim]

print("Lista editada:", numero)