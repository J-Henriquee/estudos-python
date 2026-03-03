
#Definindo variáveis 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
palavras = ['comida', 'furação', 'tufão', 'manobra', 'rei']
soma = 0
maximo = numeros[0]
#Loop para interar sobre os valores e imprimir a soma e média
for n in numeros:
    soma += n
print(f'Essa é a soma: {soma}')
print(f'Esssa é a média: {soma / len(numeros)}')
#Iterando sobre os números e imprimindo o máximo
for n in numeros:
    if n > maximo:
        maximo = n
print(maximo)

#Imprimindo palavras com pelo menos 5 cárateres 
for palavra in palavras:  
    if len(palavra) >= 5:
        print(palavra)

