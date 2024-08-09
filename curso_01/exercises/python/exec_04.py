taxaAno = 1
valorInvestimento = 200

def anosParaDuplicarInvestimento(taxaAno, valorInvestimento):
    anos = 0
    valorInvestimentoDuplicado = valorInvestimento * 2
    valorInvestimentoComJuros = valorInvestimento
    taxaAjustada = 1 + taxaAno

    while True:
        valorInvestimentoComJuros = valorInvestimentoComJuros * taxaAjustada
        anos += 1
        if valorInvestimentoComJuros >= valorInvestimentoDuplicado:
            break

    return anos


print(anosParaDuplicarInvestimento(taxaAno, valorInvestimento))