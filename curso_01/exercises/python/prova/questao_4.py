import pandas as pd


paises = pd.read_csv('../basedados/paises.csv')

paises['densidade_demografica'] =  round((paises['Populacao'] / paises['Área (km²)']))
#print(paises)

paises2 = paises.query("densidade_demografica > 1000 & Populacao > 5000000")

print(paises2)
#resultado Bangladesh, Hong Kong, Singapura