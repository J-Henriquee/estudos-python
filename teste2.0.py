nome_correto = 'Nean' 
senha_correta = '123'

nome = input('Qual seu nome de usuário? ')
senha = input('Qual a sua senha? ')
print('-' * 5 )
if nome == nome_correto:
    if senha == senha_correta:
        print('Sucesso')
    else:
        print('Senha incorreta')
else:
    if senha == senha_correta:
      print('Nome incorreto')
    else:
      print('Nome e senha incorretos')
print('-' * 5 )


