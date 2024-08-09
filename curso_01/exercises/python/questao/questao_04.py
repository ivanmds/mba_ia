prod = ('macarrao', 10.0, 2025, 7)

prods = [('macarrao', 5.99, 2025, 7),
      ('palmito', 12.50, 2027, 8),
      ('arroz', 21.50, 2025, 9),      
      ('feijao', 8.50, 2027, 10),
      ('grao de bico', 8.50, 2027, 8),
      ('feijao preto', 8.90, 2025, 7),
      ('molho', 2.50, 2025, 6),
      ('cafe', 7.30, 2025, 6),
      ('manteiga', 8.99, 2025, 7),
      ('chocolate', 2.00, 2025, 9),
      ('azeite', 10.50, 2027, 1),
      ('farinha', 3.50, 2025, 7),
      ('fuba', 4.50, 2027, 8)]


produto_promocao = lambda produto: (f'{produto[0]} em promoção', produto[1]/ 2, produto[2], produto[3])
print(produto_promocao(prod))


def gera_lista_promocao(produtos, ano, mes):
    return [produto_promocao(prod) for prod in produtos if prod[2] <= ano and prod[3] <= mes]

lista_promocao = gera_lista_promocao(prods, 2025, 8)
lista_precos = [prod[1] for prod in lista_promocao]

print(lista_promocao)
print(lista_precos)
print(min(lista_precos))
print(max(lista_precos))