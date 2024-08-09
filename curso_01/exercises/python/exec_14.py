def getLista(n):
    resultado = []
    for i, v1 in enumerate(range(0, n)):
        linha = []
        for j, v2 in enumerate(range(0, n)):
            linha.append(i + j * i)
        resultado.append(linha)
    return resultado


def getLista2(n):
    return [[i + j * i for j in range(n)] for i in range(n)]

print(getLista2(5))