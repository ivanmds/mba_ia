nomes = "ana,fábio,cristina,ana,fábio,ubiratã,ana"


def conta_palavras(texto):
    listaNomes = texto.split(',')
    dicFreq = {}
    for item in listaNomes:
        if item in dicFreq:
            dicFreq[item] += 1
        else:
            dicFreq[item] = 1
    return dicFreq

resultado = conta_palavras(nomes)
print(resultado)