import pandas

df = pandas.read_csv('basedados/WorldCups.csv') 
df['AverageGoalsMatch'] = df.apply(lambda row: row['GoalsScored'] / row['MatchesPlayed'], axis=1)

#print(df)

brazilWinner = df.query("Winner == 'Brazil'")
#print(brazilWinner)

brazilWinnerOrRunnersup = df.query("Winner == 'Brazil' or RunnersUp == 'Brazil' ")
print(brazilWinnerOrRunnersup)

totalVitoriasBrasil = len(brazilWinner.index)
totalFinaisBrasil = len(brazilWinnerOrRunnersup.index)
print(totalVitoriasBrasil)

porcentagemBrasilFinais = totalVitoriasBrasil * 100 / totalFinaisBrasil

print(porcentagemBrasilFinais)