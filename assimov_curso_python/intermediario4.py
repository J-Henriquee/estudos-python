def é_primo(n):
    if n <= 1:
        print('Não é primo')
        return

    # Calculando a raiz quadrada e transformando em inteiro
    raiz_quadrada = int(n ** 0.5) 
    
    # Testamos do 2 até a raiz quadrada (+1 para o range incluir a própria raiz)
    for i in range(2, raiz_quadrada + 1):
        if n % i == 0:
            print('Não é primo')
            return
            
    print('É primo')