#Definindo listas
lista1 = ['1', '1', -5, 'cachorro', 'cat', 1.90 ]
lista2 = ['1', '2', -5, 'cachorro', 'cat', 'Mecha', 'cat']
lista_duplicados = []
elemento_duplicado = False
#Isolamos um elemento de uma lista e comparamos  com todos os elementos da outra lista 
for elemento1 in lista1:
    for elemento2 in lista2:
        if elemento1 == elemento2:
            if elemento1 not in lista_duplicados: 
               print(f'O elemento "{elemento1}" está duplicado')
               lista_duplicados.append(elemento1)
            break
#Fazemos o mesmo que fizemos no outor loop mas agora imprimindo uma messagem diferente 
for elemento1 in lista1:
    for elemento2 in lista2:
        if elemento1 == elemento2:
            print('Há um elemento em comum entre as listas')
            elemento_duplicado = True
            break
    if elemento_duplicado:
        break