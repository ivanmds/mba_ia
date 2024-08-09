import math

def multiplica_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        print("listas devem ser do mesmo tamanho")
        return math.nan
    
    return [lista2[i] * v for i, v in enumerate(lista1)]
    

l1 = [1, 2, 3, 4, 5]
l2 = [5, 5, 5, 10, 10]

print(multiplica_listas(l1,l2))