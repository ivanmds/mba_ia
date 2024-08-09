#continuar aula 12

import random
import statistics

produtos = [('soja', [170.1, 183.0, 175.0]),
            ('algodao', [143.4]),
            ('cacau', [199, 185.1]),
            ('café', [880, 750.9, 795.1, 900])]

preco_medio = [(item[0], statistics.mean(item[1])) for item in produtos]
sorteio_index = random.randint(0, len(preco_medio) - 1)

print(preco_medio[sorteio_index])

