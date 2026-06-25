alfabetoMA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
alfabetoMI = "abcdefghijklmnopqrstuvwxyz" 
#Solicita o texto padrão para o usuário
texto = list(input('Digite aqui o texto a ser cripitografado: '))
#Obrigamos o usuário a digitar algum número 
while True:
      try:
          chave = int(input('Digite aqui a chave desejada (Apenas números): '))
          break
      except: 
          print('Use apenas números!')
#Iteramos sobre o texto padrão em busca de cada letra e em seguida passamos a chave e mudamos sua posição       
for i1, c in enumerate(texto):
    # Encontra o índice base
    indice_base = alfabetoMA.find(c.upper())
    
    # Se não for uma letra (tipo espaço ou pontuação), o find retorna -1. 
    # O seu código original lidava com isso super bem ignorando na hora do if!
    
    # O % 26 garante que, não importa o tamanho da chave, o resultado sempre caia entre 0 e 25!
    i2 = (indice_base + chave) % 26
    
    if c in alfabetoMA:
        texto[i1] = alfabetoMA[i2]
    
    if c in alfabetoMI:
       texto[i1] = alfabetoMI[i2]
#Como strings são imutáveis nós passamos tínhamos convertido para uma lista e agora volta a ser uma string com o metódo join
print(''.join(texto))
