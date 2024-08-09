import pandas as pd

worldCupMatches = pd.read_csv('../basedados/WorldCupMatches.csv')

#print(worldCupMatches)

def filtroPorTime(nomeTime):
    return worldCupMatches.query(f'HomeTeamName == "{nomeTime}" or AwayTeamName == "{nomeTime}"')

partidasFiltradas = filtroPorTime('Scotland')

print(len(partidasFiltradas))
print(partidasFiltradas[:3])