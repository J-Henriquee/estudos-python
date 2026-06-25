# def exibir(*args, **kwargs):
#    print(args)
#    print(kwargs)


# valores = [1, 2, 3]
# dict = {'Nome': 'Nean', 'Stack' : 'Python'}

# exibir(1, 2, 3, valores, **dict)


# x = 12

# if isinstance(x, str):
 #   print('É uma string')
# else:
#     print(type(x))
#numeros = [3, 6, 10]
#numeros = [numero + 2 for numero in numeros]

 

#filtro = filter(lambda x: x >= 0, [10, 2, 4, -4, -5])

#list(filtro)
 
#def vezes2(x):
#    return x*2

#def meu_decorador(func):
#    def meu_pacote(*args, **kwargs):
#        retorno = func(*args, **kwargs)
#        return retorno*2
#    return meu_pacote
  
#vezes2 = meu_decorador(func = vezes2)

#print(vezes2(32))

#@meu_decorador
#def vezes2(x):
#    return x*2
#import functools

#def imprimir_recibo(func):
  
#    def meu_pacote(*args, **kwargs):
#        print("--- INICIANDO COMPRA ---")

#        retorno = func(*args, **kwargs)
#        print("--- COMPRA FINALIZADA ---")
#        return retorno

#    return meu_pacote


#@imprimir_recibo
#@functools.cache
#def fechar_carrinho(*args, **kwargs):
#    valor_desconto = kwargs.get('desconto', 0)
#    total = sum(args) - valor_desconto
#    return total 
    

#total = fechar_carrinho(10, 50, 40, desconto=10)


#print(total)


valores = [1, 2, 3, 5, 10]

quadrados_maiores_que_tres = []
for valor in valores:
    if valor > 3:
        quadrado = valor ** 2
        quadrados_maiores_que_tres.append(quadrado)
print(quadrados_maiores_que_tres)
quadrados_maiores_que_tres = [ valor ** 2 for valor in valores if valor > 3 ]

print(quadrados_maiores_que_tres)
quadrados_maiores_que_tres = list(map(lambda x: x ** 2, filter(lambda x: x > 3, valores)))

print(quadrados_maiores_que_tres)


