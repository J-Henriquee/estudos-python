
print('-----Seja bem-vindo ao jogo dos estados!-----')
capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas',
    'Distrito Federal': 'Brasília'
}
perguntas_respondidas = 0 
contador_acertos = 0
for estado in capitais:
    
    guess = input(f'Qual a capital do estado: {estado}\nDigite E para sair do jogo: ')

    if guess.strip().upper() == 'E':
        break
    if guess.lower().strip() == capitais[estado].lower().strip():
        
        print('Parabéns, você acertou!')
        contador_acertos += 1
    else:
        print(f'Você errou! A resposta correta era {capitais[estado]}')
    perguntas_respondidas += 1
if perguntas_respondidas > 0:
    porcentagem = round(100 * (contador_acertos / perguntas_respondidas ))
    print(f'Seu numero de acertos foi {contador_acertos} e sua porcentagem de acertos foi {porcentagem}%')
else:
    print(f'Seu numero de acertos foi {contador_acertos} e sua porcentagem de acertos foi 0%')









arquivos = ['ei.pdf', 'nei.jpg', '2024.pdf', 'nah.docx']

arquivos_pdf = [arquivo for arquivo in  arquivos if arquivo.endswith('pdf') ]

print(arquivos_pdf)