import pandas

df = pandas.read_csv('basedados/WorldCups.csv') 
df = df.drop('QualifiedTeams', axis=1)
df = df.drop('Fourth', axis=1)
df = df.query('Year >= 1954 & Year <= 1982')

print(df)