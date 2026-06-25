import numpy as np

n = 3
# Cria uma matriz 3x3 preenchida com o caractere ""
grade = np.full((n, n), "")


class Tabuleiro:
    def __init__(self, jogo):
        self.imprimir_tab = print(jogo)

    def fazer_jogada(self, posição1, posição2, jogador, grade = grade):
        if grade[posição1,posição2] != '':
            print('A posição já está ocupada')
            return False
        if jogador == 1:
            grade[posição1,posição2] = 'X'
        else:
            grade[posição1,posição2] = 'O'
        return True
    def verificar_vencedor(self, grade = grade):
        lista1 = ['X', 'X', 'X']
        lista2 = ['O', 'O', 'O']
        lista_diagonal_inver = [grade[3,1], grade[2,2], grade[1,3]]
        venceu1 = lista_diagonal_inver  == lista1
        venceu2 = lista_diagonal_inver  == lista2

        if venceu1:
            return 1
        if venceu2: 
            return 2

        if lista1 or lista2 in grade:
           if 'X' in grade:
               return 1
           elif 'O' in grade:
               return 2 
               
        if not venceu1 or not venceu2:
            parar = False
            for i in range(3):
                if parar:
                    break
                lista_coluna = []
                for j in range(3):
                    lista_coluna.append(grade[j, i])
                    if i == j:
                        lista_diagonal.append(grade(i, j))
                if lista_coluna == lista1 or lista_diagonal == lista1: 
                    venceu1 = True
                    parar = True
                    break
                if lista_coluna == lista2 or lista_diagonal == lista2:
                    venceu2 = True
                    parar = True
                    break
            if not venceu1 or not venceu2:
                for i in range(3):
                    lista_diagonal = []
                    for j in range(3):
                        if i == j:
                            lista_diagonal.append(grade(j, i))
                    

self =  Tabuleiro(grade)

self.imprimir_tab

