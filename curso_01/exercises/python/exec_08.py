import pandas

df = pandas.read_csv('basedados/WorldCups.csv') 
df_indexado = df.set_index('Year')


print(df_indexado.iloc[:6])

# finalizar não entendi muito bem o que esta pedindo com 
#- Exiba o tipo de dado de cada coluna
#- Imprima o número de linhas do DataFrame