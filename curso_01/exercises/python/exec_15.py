nomes = ['Dennis ritchie', 'ALAN Turing', 'betty Holberton']

resultado = [nome.split(" ")[-1].upper() + ", " + nome.split(" ")[0].upper()[0]  + "." for nome in nomes]

resultado2 = [f"{last.upper()}, {first[0].upper()}." for nome in nomes for first, *_, last in [nome.split()]]


print(resultado2)