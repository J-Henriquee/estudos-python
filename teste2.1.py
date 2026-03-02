print('---Primeira tentativa!---')
numero_secreto = 8
acertou = False

numero = int(input('Adivinhe o número\nDigite aqui: '))
if numero > numero_secreto:
    print('Você errou! seu número adivinhado é maior que o secreto')
elif numero < numero_secreto:
    print('Você errou! seu número adivinhado é menor que o secreto')
else:
    print('Parabéns, você acertou!')
    acertou = True
    
if not acertou:
    print('---Segunda tentativa!---')
    numero = int(input('Adivinhe o número\nDigite aqui: '))
    if numero > numero_secreto: 
       print('Você errou! seu número adivinhado é maior que o secreto')
    elif numero < numero_secreto:
        print('Você errou! seu número adivinhado é menor que o secreto')
    else:
        print('Parabéns, você acertou!') 
        acertou = True
 
if not acertou:
    print('---Ùltima tentativa!---')
    numero = int(input('Adivinhe o número\nDigite aqui: '))
    if numero != numero_secreto:
        print(f'Você errou! O número secreto era {numero_secreto}')
    else:
        print('Parabéns, você acertou!') 
 



