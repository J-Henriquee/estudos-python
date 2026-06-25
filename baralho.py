import random
# Criando as 52 cartas padrão
baralho = [v + n for n in ['♥', '♦', '♠', '♣'] for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]




def gerar_baralho(cópias, coringas: bool = 0, embaralhar: bool = 0, baralho: list[str] = baralho):
    for _ in range(cópias - 1):

        baralho += baralho
    
    if coringas:
        for _ in range(cópias):
            baralho.extend(('JK2', 'JK2'))

    print(baralho)

    if embaralhar:
        random.shuffle(baralho)

    print(baralho)

    return baralho


def mostrar_baralho(baralho_novo):
    print(baralho_novo)

def dar_as_cartas(x, y, baralho_novo):
    cartas_jogadores = []
    for _ in range(x):
        cartas_jogadorn = baralho_novo[:y]
        del baralho_novo[:y]
        cartas_jogadores.append(cartas_jogadorn)
        cartas_jogadorn = []
    print(cartas_jogadores)
    return cartas_jogadores



def mostrar_jogadores(cartas_jogadores):
    for i, c in enumerate(cartas_jogadores):
        print(f'O Jogador {i + 1}  possui as seguintes cartas:\n{c}\n')


def verificar_int(resultado):
    try:
        valor = int(resultado)
        if valor > 0:
            return valor 
        else:
            print('Digita apenas números positivos')
            return ''
    except:
        print('O valor digitado é inválido')
        return ''

coringas1 = ''
cópias1 = ''
embaralhar1 = ''


while coringas1 not in[0, 1] and embaralhar1 not in [0, 1] and type(cópias1) != int:

    
    if type(cópias1) != int:
        cópias1 = verificar_int(input('Quantas cópias do baralho você usará? '))
    
    if  coringas1 not in[0, 1]:
        coringas1 = input('Deseja coringas no baralho?(Tecle S ou N) ')
    if coringas1.upper == 'S':
        coringa1 = 1
    if coringas1.upper == 'N':
        coringa1 = 0

    if  embaralhar1 not in[0, 1]:
        embaralhar1 = input('Deseja embaralhar o baralho?(Tecle S ou N) ')
    if embaralhar1.upper == 'S':
        embaralhar1 = 1
    if embaralhar1.upper == 'N':
        embaralhar1 = 0
jogadores = ''
cartas = ''
baralho_novo = gerar_baralho(cópias1, coringas1, embaralhar1,)

quantidade_compativel = None



while type(jogadores) != int and type(cartas) != int and not quantidade_compativel:
    
    if  type(jogadores) != int:
        jogadores = verificar_int(input('Quantos jogadores você deseja? '))

    if type(cartas) != int:
        cartas = verificar_int(input('Quantas cartas para cada jogador? '))
    
    if type(jogadores) == int and type(cartas) == int:
        quantidade_compativel = ((cartas * jogadores) % len(baralho_novo)) > cartas  or (cartas * jogadores)  % len(baralho) == 0
        if quantidade_compativel:
            break
        else:
             print('Um ou mais jogadores ficaram com menos cartas')
             jogadores = verificar_int(input('Quantos jogadores você deseja? '))
             cartas = verificar_int(input('Quantas cartas para cada jogador ?'))




mostrar_baralho(baralho_novo)

cartas_jogadores  = dar_as_cartas(jogadores, cartas, baralho_novo)

mostrar_jogadores(cartas_jogadores)
