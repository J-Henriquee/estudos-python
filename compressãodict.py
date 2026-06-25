palavras = ['Olá', 'Python', 'Juliano', 'Asimov Academy']
dict_caracteres = {palavra.lower(): len(palavra.replace(' ', '')) for palavra in palavras}
print(dict_caracteres)
