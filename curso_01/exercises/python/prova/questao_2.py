lv = [('BRA', 'DFD-2992', 12, 2031, 999.0),
      ('ARG', '1112992', 1, 2032, 899.0),
      ('EUA', 'AB3DA000', 11, 2031, 1023.0),
      ('BRA', 'GCG-1112', 9, 2031, 900.0),
      ('ESP', 'DFD-2992', 11, 2031, 899.0),
      ('URU', 'AEC423', 3, 2033, 699.0),
      ('PAR', 'DFD-2992', 2, 2035, 1099.0),
      ('ARL', 'X123111Z', 10, 2031, 954.0),
      ('URU', 'BAC203', 2, 2035, 1011.0),
      ('ARG', '3112323', 10, 2031, 1250.0),
      ('URU', 'ABC123', 12, 2034, 1001.5),
      ('BRA', 'AAB-2992', 8, 2031, 1050.9),
      ('BRA', 'EFE-2992', 8, 2032, 1170.1),
      ('VEN', 'GAC292', 4, 2033, 1000.6),
      ('PER', '2992DDE', 9, 2031, 989.9)]

totalVogais = 0
vogais = "aeiouAEIOU"

for item in lv:
    for word in item[1]:
        if vogais.find(word) >= 0:
            print(f"{item[1]} with vogal {word}")
            totalVogais+=1

print(f"total vogais {totalVogais}")
#resultado 12