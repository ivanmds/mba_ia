#import numpy as np

l_tup = [('a',[8, 4, 6, 1]), ('b',[1, 2, 3, 4]), ('c',[5, 3, 3, 3])]
resultado = [v[1] for i,v in enumerate(l_tup)]
print(resultado)

for i in resultado:
    print(f"{i[-3]} {i[-2]} {i[-1]}")