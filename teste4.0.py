
#Texto base e vogais para resolução 
texto = "O Python foi concebido no final de 1989 por Guido van Rossum no CWI (Holanda), lançado em 1991 como um hobby de Natal para substituir a linguagem ABC. Focada na legibilidade, simplicidade e flexibilidade, a linguagem foi inspirada no grupo de comédia Monty Python. Evoluiu com grandes marcos como a versão 2.0 (2000) e 3.0 (2008), tornando-se popular em IA e web."
vogais = ['a', 'e', 'i', 'o', 'u', 'é', 'ê', 'á', 'à', 'â', 'ã', 'ó', 'ô', 'õ', 'í', 'ú']
count_vogais = 0
#Nosso loop itera sobre as vogais e adiciona  no contador total quando encontra uma.
for vogal in vogais:
    count_vogais += texto.lower().count(vogal)

print(count_vogais)


