import math
import random as rd

vetor = [rd.randint(0, 100) for _ in range(0, 10)]
resultado = [math.log(x) if x != 0 else math.nan for x in  vetor]
print(resultado)