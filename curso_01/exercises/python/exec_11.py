import numpy as np

def getLista(n, passo):
    lista = np.zeros((n))
    for (idItem, vItem) in enumerate(lista):
        if idItem > 0:
            lista[idItem] = round(lista[idItem - 1] + passo, 5)
    return lista

def getLista2(n, passo):
    return np.array([round(i * passo, 5) for i in range(n)])


print(getLista2(10, 0.5))
    
