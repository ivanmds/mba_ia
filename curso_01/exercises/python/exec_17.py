import random

resultado = [[random.randint(1,5) for _ in range(6)] for _ in range(10)]
print(resultado)

resultado2 = [r[2:] for r in resultado]
print(resultado2)

resultado3 = [resultado2[2], resultado2[5], resultado2[8]]
print(resultado3)

resultado4 = [y for x in resultado3 for y in x if y >= 4]
print(resultado4)