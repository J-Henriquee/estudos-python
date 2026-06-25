def multiplicar_por(x):
    def multiplicadora(n):
        resultado = x*n 
        return resultado
    return multiplicadora


dobrar = multiplicar_por(2)

print(dobrar(4))
vezes_cinco = multiplicar_por(5)
print(vezes_cinco(4))