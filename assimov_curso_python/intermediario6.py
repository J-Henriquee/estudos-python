import itertools

comidas = {
    'Prato Feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90,
}

bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90,
}

combinações = [combo for combo in itertools.product(comidas, bebidas)]
valores =[valor for valor in itertools.product(comidas.values(), bebidas.values())]
combos = {}
combinação = [combinação for combinação in itertools.zip_longest(combinações, valores)]
for i, value in enumerate(combinação):
    value = round((combinação[i][1][0] + combinação[i][1][1]), 2)
    combos.update({tuple(combinação[i][0]): value})

print(combos)








 