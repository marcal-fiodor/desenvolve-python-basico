#Pares
pares = [x for x in range(20, 51) if x % 2 == 0]
print(pares)
#Potência
quadrados = [n**2 for n in [1,2,3,4,5,6,7,8,9]]
print(quadrados)
#Divisiveis por 7
divisiveis = [x for x in range(1, 101) if x % 7 == 0]
print(divisiveis)
#Par ou impar
par_impar = ["Par" if x % 2 == 0 else "Impar" for x in range(0,30,3)]
print(par_impar)