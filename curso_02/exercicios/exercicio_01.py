import pandas as pd
import statistics as stc
df = pd.read_csv('../arquivos/jogadores_exercicio1.csv')

coluna_1 = "weight"
coluna_2 = "age"

print("\n")
print("Média weight " + str(stc.mean(df[coluna_1])))
print("Desvio padrão weight " + str(stc.pstdev(df[coluna_1])))

print("\n")

print("Média age " + str(stc.mean(df[coluna_2])))
print("Desvio padrão age " + str(stc.pstdev(df[coluna_2])))

#resposta a