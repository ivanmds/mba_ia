import pandas as pd
import numpy as np

partidas = pd.read_csv('../basedados/WorldCupMatches.csv')


def jogospaises(pais1, pais2, partidas):
    partidasFiltrada = partidas.query(f'HomeTeamName == "{pais1}" & AwayTeamName == "{pais2}"')
    partidasFiltrada2 = partidas.query(f'HomeTeamName == "{pais2}" & AwayTeamName == "{pais1}"')
    anosPartidas =  partidasFiltrada['Year'].to_numpy()
    anosPartidas2 = partidasFiltrada2['Year'].to_numpy()
    #print(partidasFiltrada)
    print(anosPartidas)
    print(anosPartidas2)

jogospaises('Brazil', 'England', partidas)
# resultada [1958, 1962, 1970, 2002]ls