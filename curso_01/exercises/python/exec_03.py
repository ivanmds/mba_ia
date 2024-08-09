valores = ['três', 56, 342, 12.4e-5, 4+3j, ('A', 1, 50.1), -0.19e4, 1000, 960, -406]
numeros = []


for valor in valores:
    if type(valor) == int:
        numeros.append(valor)

print(numeros)