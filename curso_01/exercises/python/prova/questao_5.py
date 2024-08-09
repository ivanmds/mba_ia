import pandas as pd
df = pd.read_csv('../basedados/CPI2023-Global-Results-Trends.csv')
df.head()

df2 = df.dropna()
#print(df2.to_numpy())
df22 = df2.to_numpy()
df3 = []
totalIgnorada = 0;

for item in df22:

    if len(item) >=11:
        df3.append(item)
    else:
        totalIgnorada+=1

    print(f"{item[2]/item[7]} e {item[2]/item[9]}")

print(len(df3))
# não sei eu iria na opcao b ou d