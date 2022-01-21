import pygame
from pygame.locals import *

pygame.init()

tela = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption("INCLUSIONGAME - VENCENDO OBSTÁCULOS")

# IMAGENS
img_user1 = pygame.image.load("imagens/cadeirante3.png").convert_alpha()
img_user2 = pygame.image.load("imagens/cadeirante4.png").convert_alpha()
img_user3 = pygame.image.load("imagens/visual1.png").convert_alpha()
img_user4 = pygame.image.load("imagens/visual2.png").convert_alpha()
img_user5 = pygame.image.load("imagens/libras1.png").convert_alpha()
img_user6 = pygame.image.load("imagens/libras2.png").convert_alpha()
img_fundo = pygame.image.load("imagens/fundo3.png").convert_alpha()
img_fundo2 = pygame.image.load("imagens/fundo4.png").convert_alpha()
img_fundo3 = pygame.image.load("imagens/fundo5.png").convert_alpha()
comojogar_fundo = pygame.image.load("imagens/COMOJOGAR.png").convert_alpha()
sobre_fundo = pygame.image.load("imagens/SOBRE.png").convert_alpha()
menu = pygame.image.load("imagens/menu.png").convert_alpha()
fim = pygame.image.load("imagens/fim.png").convert_alpha()
final = pygame.image.load("imagens/final.png").convert_alpha()
fase1 = pygame.image.load("imagens/ComoJogarFase1.png").convert_alpha()
fase2 = pygame.image.load("imagens/ComoJogarFase2.png").convert_alpha()
fase3 = pygame.image.load("imagens/ComoJogarFase3.png").convert_alpha()
click = pygame.image.load("imagens/click1.png").convert_alpha()

# AUDIOS

pygame.mixer.music.load("audios/action2.mp3")
pygame.mixer.music.play(5)
pygame.mixer.music.set_volume(0.3)
som_buraco = pygame.mixer.Sound("audios/cuidadoburaco.ogg")
som_lixo = pygame.mixer.Sound("audios/lixo1.ogg")
som_escada = pygame.mixer.Sound("audios/naosubir2.ogg")
som_arvore = pygame.mixer.Sound("audios/naopassar.ogg")
aplausos = pygame.mixer.Sound("audios/aplausos.ogg")
som_libras1 = pygame.mixer.Sound("audios/librasnao.ogg")
som_libras2 = pygame.mixer.Sound("audios/librassim.ogg")


cor_roxa = (25, 25, 112)
ret = pygame.Rect(5, 5, 50, 50)
jogador = [60, 180, 59, 59, 0]


#Fase 1 - X, Y, Largura, Altura, Abertura disponível [direção, abertura]]
road1 = [50, 180, 180, 80,
         [[4, 149, 251, 1]]]
road2 = [150, 260, 80, 130, [[2, 149, 241, 0], [4, 149, 241, 2]]]
road3 = [50, 390, 240, 80, [[2, 149, 241, 1], [4, 149, 241, 3], [3, 389, 471, 5]]]
road4 = [150, 470, 80, 130, [[2, 149, 231, 2], [4, 149, 231, 4]]]
road5 = [150, 600, 140, 80, [[2, 149, 231, 3], [3, 599, 682, 6]]]
road6 = [290, 390, 140, 80, [[1, 389, 471, 2], [2, 340, 440, 8], [3, 389, 471, 11], [4, 340, 440, 9]]]
road7 = [290, 600, 290, 80, [[1, 599, 682, 4], [2, 345, 435, 9], [4, 499, 581, 10], [3, 599, 681, 13]]]
road8 = [350, 180, 80, 80, [[4, 349, 431, 14]]]
road9 = [350, 240, 80, 150, [[4, 349, 431, 5], [3, 229, 320, 14], [2, 350, 430, 7]]]
road10 = [350, 470, 80, 130, [[2, 345, 435, 2], [4, 345, 435, 4]]]
road11 = [500, 680, 80, 170, [[2, 499, 581, 4]]]
road12 = [430, 390, 390, 80, [[1, 389, 471, 5], [4, 719, 801, 12]]]
road13 = [720, 470, 80, 130, [[2, 719, 801, 11], [4, 719, 801, 13]]]
road14 = [580, 600, 600, 80, [[1, 600, 680, 6], [2, 719, 801, 12], [3, 599, 681, 25], [4, 1100, 1180, 27]]]
road15 = [431, 240, 330, 80, [[1, 239, 321, 8], [3, 239, 321, 15]]]
road16 = [760, 160, 80, 160, [[1, 239, 321, 14], [3, 150, 241, 16]]]
road17 = [840, 160, 240, 80, [[1, 160, 240, 15], [3, 150, 241, 17]]]
road18 = [1080, 160, 290, 80, [[1, 159, 241, 16], [4, 1180, 1260, 18], [3, 159, 241, 20]]]
road19 = [1180, 240, 80, 150, [[2, 1180, 1260, 17], [4, 1180, 1260, 19]]]
road20 = [900, 390, 560, 80, [[2, 1180, 1260, 18], [3, 389, 471, 22], [4, 1380, 1460, 23]]]
road21 = [1370, 160, 300, 80, [[1, 159, 241, 17]]]
road22 = [1590, 240, 80, 150, [[2, 1590, 1670, 20], [4, 1590, 1670, 22]]]
road23 = [1460, 390, 410, 80, [[1, 389, 471, 19], [4, 1790, 1870, 24]]]
road24 = [1380, 470, 80, 130, [[2, 1380, 1460, 19], [4, 1380, 1460, 25]]]
road25 = [1790, 470, 80, 130, [[2, 1790, 1870, 22], [4, 1790, 1870, 26]]]
road26 = [1180, 600, 470, 80, [[1, 599, 681, 13], [2, 1380, 1460, 23], [4, 1550, 1630, 28]]]
road27 = [1740, 600, 130, 80, [[2, 1790, 1870, 24], [4, 1790, 1870, 29]]]
road28 = [1100, 680, 80, 120, [[2, 1100, 1180, 13], [4, 1100, 1180, 30]]]
road29 = [1550, 680, 80, 120, [[2, 1550, 1630, 25], [4, 1550, 1630, 31]]]
road30 = [1790, 680, 80, 310, [[2, 1790, 1870, 26], [1, 800, 880, 31]]]
road31 = [1100, 800, 230, 80, [[2, 1100, 1180, 27]]]
road32 = [1390, 800, 400, 80, [[2, 1550, 1630, 28], [3, 800, 880, 29]]]
buraco1 = [600, 600, 70, 80]
buraco2 = [1380, 510, 80, 40]
escada1 = [800, 390, 40, 80]
escada12 = [860, 390, 60, 80]
escada2 = [1640, 600, 40, 80]
escada22 = [1720, 600, 40, 80]
arvore1 = [1310, 800, 30, 80]
arvore12 = [1370, 800, 40, 80]
arvore2 = [1590, 220, 80, 40]
arvore22 = [1590, 360, 80, 40]
casa = [1790, 970, 80, 60]


roadList = [road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, road11, road12, road13, road14, road15, road16, road17, road18, road19, road20,
            road21, road22, road23, road24, road25, road26, road27, road28, road29, road30, road31, road32]

road01 = [100, 140, 400, 80, [[4, 279, 361, 1], [3, 139, 221, 10]]]
road02 = [280, 220, 80, 690, [[2, 279, 361, 0], [1, 480, 561, 2], [4, 279, 361, 3], [3, 639, 721, 15]]]
road03 = [100, 480, 180, 80, [[3, 480, 561, 1]]]
road04 = [280, 910, 450, 80, [[2, 279, 361, 1], [3, 909, 991, 4]]]
road05 = [730, 720, 80, 270, [[1, 909, 991, 3], [2, 729, 811, 19], [3, 909, 991, 5]]]
road06 = [810, 910, 650, 80, [[1, 909, 991, 4], [3, 909, 991, 6], [2, 1059, 1141, 16]]]
road07 = [1460, 720, 80, 270, [[1, 909, 991, 5], [3, 909, 991, 7], [2, 1459, 1541, 17]]]
road08 = [1540, 910, 270, 80, [[1, 909, 991, 6], [2, 1729, 1811, 8]]]
road09 = [1730, 480, 80, 430, [[4, 1729, 1811, 7], [1, 479, 561, 14], [2, 1729, 1811, 9]]]
road010 = [1730, 210, 80, 270, [[4, 1729, 1811, 8], [1, 209, 291, 18]]]
road011 = [500, 140, 80, 340, [[1, 139, 221, 0], [4, 499, 581, 11]]]
road012 = [500, 480, 230, 80, [[2, 499, 581, 10], [3, 479, 561, 12]]]
road013 = [730, 480, 420, 80, [[1, 479, 561, 11], [4, 729, 811, 19], [2, 1069, 1151, 13], [3, 479, 561, 14]]]
road014 = [1070, 140, 80, 340, [[4, 1069, 1151, 12]]]
road015 = [1150, 480, 580, 80, [[1, 479, 561, 12], [3, 479, 561, 8]]]
road016 = [360, 640, 370, 80, [[1, 639, 721, 1], [3, 639, 721, 19]]]
road017 = [1060, 640, 80, 270, [[4, 1059, 1141, 5], [3, 639, 721, 17]]]
road018 = [1140, 640, 400, 80, [[1, 639, 721, 16], [4, 1459, 1541, 6]]]
road019 = [1570, 210, 160, 80, [[3, 209, 291, 9]]]
road020 = [730, 560, 80, 160, [[1, 639, 721, 19], [2, 729, 811, 12], [4, 729, 811, 4]]]
buraco3 = [1190, 480, 10, 80]
buraco4 = [400, 640, 10, 80]
lixo1 = [730, 558, 80, 20]
lixo12 = [730, 610, 80, 20]
lixo2 = [1380, 910, 80, 20]
lixo22 = [1420, 910, 40, 20]
casa2 = [1570, 210, 40, 80]

road2List = [road01, road02, road03, road04, road05, road06, road07, road08, road09, road010, road011, road012, road013, road014, road015, road016, road017, road018, road019, road020]

road001 = [130, 140, 80, 780, [[3, 279, 361, 1]]]
road002 = [210, 280, 250, 80, [[1, 279, 361, 0], [3, 279, 361, 5], [4, 379, 461, 2]]]
road003 = [380, 360, 80, 450, [[2, 379, 461, 1], [3, 539, 621, 3], [4, 379, 461, 10]]]
road004 = [460, 540, 500, 80, [[1, 539, 621, 2], [3, 539, 621, 6]]]
road005 = [460, 840, 280, 80, [[1, 839, 920, 10]]]
road006 = [460, 280, 710, 80, [[1, 279, 361, 1], [3, 279, 361, 7], [4, 959, 1041, 6]]]
road007 = [960, 360, 80, 560, [[2, 959, 1041, 5], [1, 539, 621, 3], [3, 839, 921, 9]]]
road008 = [1170, 280, 600, 80, [[1, 279, 361, 5], [4, 1309, 1391, 8]]]
road009 = [1310, 360, 80, 480, [[2, 1309, 1391, 7], [4, 1309, 1391, 9]]]
road0010 = [1040, 840, 730, 80, [[1, 839, 921, 6], [2, 1309, 1391, 8]]]
road0011 = [380, 810, 80, 110, [[2, 379, 461, 2], [3, 839, 921, 4]]]
escola1 = [660, 840, 80, 80]
escola2 = [1680, 840, 20, 80]

road3List = [road001, road002, road003, road004, road005, road006, road007, road008, road009, road0010, road0011]


def moverJogador(left, up, rigth, down, player, roadList):
    if left and colisaoLeftCaminho(player, roadList, player[4]):
        player[0] -= 1.2
    if up and colisaoUpCaminho(player, roadList, player[4]):
        player[1] -= 1.2
    if rigth and colisaoRightCaminho(player, roadList, player[4]):
        player[0] += 1.2
    if down and colisaoDownCaminho(player, roadList, player[4]):
        player[1] += 1.2

def moverJogador2(left, up, rigth, down, player, road2List):
    if left and colisaoLeftCaminho2(player, road2List, player[4]):
        player[0] -= 1.5
    if up and colisaoUpCaminho2(player, road2List, player[4]):
        player[1] -= 1.5
    if rigth and colisaoRightCaminho2(player, road2List, player[4]):
        player[0] += 1.5
    if down and colisaoDownCaminho2(player, road2List, player[4]):
        player[1] += 1.5

def moverJogador3(left, up, rigth, down, player, road3List):
    if left and colisaoLeftCaminho3(player, road3List, player[4]):
        player[0] -= 1.2
    if up and colisaoUpCaminho3(player, road3List, player[4]):
        player[1] -= 1.2
    if rigth and colisaoRightCaminho3(player, road3List, player[4]):
        player[0] += 1.2
    if down and colisaoDownCaminho3(player, road3List, player[4]):
        player[1] += 1.2


def collisionDown(player, object):
    canMove = True

    if object[0] < player[0]+player[2] and object[0]+object[2] > player[0]:
        if not object[1] + object[3] < player[1]:
            if (player[1] + player[3] )+1 >= object[1]:
                canMove = False

    return canMove


def collisionUP(player, object):
    canMove = True

    # verifico se está dentro da mesma coluna que o obstáculo
    if object[0] < player[0]+player[2] and object[0]+object[2] > player[0]:
        #verifico se já está acima do obstáculo
        if not player[1] + player[3] < object[1]:
            # verificando se o próximo passo irá colidir com o objeto
            if player[1]-1 <= object[1]+object[3]:
                canMove = False

    return canMove


def collisionRight(player, object):
	canMove = True

	if (object[1] < player[1]+player[3] and object[1]+object[3] > player[1]):
		print("mesma linha do objeto")
		if not player[0] > object[0] + object[2]:
			print("está a esquerda do objeto")
			if (player[0]+player[2])+1 >= object[0]:
				print("colidiu")
				canMove = False

	return canMove

def collisionLeft(player, object):
	canMove = True

	if (object[1] < player[1]+player[3] and object[1]+object[3] > player[1]):
		print("mesma linha do objeto")
		if not player[0] + player[2] < object[0]:
			print("está a direita do objeto")
			if player[0]-1 <= object[0]+object[2]:
				print("colidiu")
				canMove = False

	return canMove


def colisaoDownCaminho(player, roadList, roadIndex):
    canMove = True
    caminhoSaida = [-1]
    if (player[1] + player[3]) + 1 >= roadList[roadIndex][1] + roadList[roadIndex][3]:
        if roadList[roadIndex][4] != -1:
            for road in roadList[roadIndex][4]:
                if road[0] == 4:
                    caminhoSaida = road
                    break

            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[0] and caminhoSaida[2] > player[0] + player[2]):
                    canMove = False
                else:
                    if player[1] + 1 > roadList[roadIndex][1] + roadList[roadIndex][3]:
                        print("Road antigo do player:", player[4])

                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False

    return canMove

def colisaoDownCaminho2(player, road2List, roadIndex2):
    canMove = True
    caminhoSaida = [-1]
    if (player[1] + player[3]) + 1 >= road2List[roadIndex2][1] + road2List[roadIndex2][3]:
        if road2List[roadIndex2][4] != -1:
            for road in road2List[roadIndex2][4]:
                if road[0] == 4:
                    caminhoSaida = road
                    break

            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[0] and caminhoSaida[2] > player[0] + player[2]):
                    canMove = False
                else:
                    if player[1] + 1 > road2List[roadIndex2][1] + road2List[roadIndex2][3]:
                        print("Road antigo do player:", player[4])

                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False

    return canMove


def colisaoDownCaminho3(player, road3List, roadIndex3):
    canMove = True
    caminhoSaida = [-1]
    if (player[1] + player[3]) + 1 >= road3List[roadIndex3][1] + road3List[roadIndex3][3]:
        if road3List[roadIndex3][4] != -1:
            for road in road3List[roadIndex3][4]:
                if road[0] == 4:
                    caminhoSaida = road
                    break

            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[0] and caminhoSaida[2] > player[0] + player[2]):
                    canMove = False
                else:
                    if player[1] + 1 > road3List[roadIndex3][1] + road3List[roadIndex3][3]:
                        print("Road antigo do player:", player[4])

                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False

    return canMove


def colisaoUpCaminho(player, roadList, roadIndex):

    canMove = True
    caminhoSaida = [-1]

    if player[1] - 1 <= roadList[roadIndex][1]:
        if roadList[roadIndex][4] != -1:
            for road in roadList[roadIndex][4]:

                if road[0] == 2:
                    caminhoSaida = road
                    break
            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[0] and caminhoSaida[2] > player[0] + player[2]):
                    canMove = False
                else:
                    if (player[1] + player[3]) - 1 > roadList[roadIndex][1]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False
        else:
            canMove = False

    return canMove


def colisaoUpCaminho2(player, road2List, roadIndex2):

    canMove = True
    caminhoSaida = [-1]

    if player[1] - 1 <= road2List[roadIndex2][1]:
        if road2List[roadIndex2][4] != -1:
            for road in road2List[roadIndex2][4]:

                if road[0] == 2:
                    caminhoSaida = road
                    break
            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[0] and caminhoSaida[2] > player[0] + player[2]):
                    canMove = False
                else:
                    if (player[1] + player[3]) - 1 > road2List[roadIndex2][1]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False
        else:
            canMove = False

    return canMove

def colisaoUpCaminho3(player, road3List, roadIndex3):

    canMove = True
    caminhoSaida = [-1]

    if player[1] - 1 <= road3List[roadIndex3][1]:
        if road3List[roadIndex3][4] != -1:
            for road in road3List[roadIndex3][4]:

                if road[0] == 2:
                    caminhoSaida = road
                    break
            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[0] and caminhoSaida[2] > player[0] + player[2]):
                    canMove = False
                else:
                    if (player[1] + player[3]) - 1 > road3List[roadIndex3][1]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False
        else:
            canMove = False

    return canMove


def colisaoRightCaminho(player, roadList, roadIndex):
    canMove = True
    caminhoSaida = [-1]

    if (player[0] + player[2]) + 1 >= roadList[roadIndex][0] + roadList[roadIndex][2]:
        if roadList[roadIndex][4] != -1:
            for road in roadList[roadIndex][4]:
                if road[0] == 3:
                    caminhoSaida = road
                    break

            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[1] and caminhoSaida[2] > player[1] + player[3]):
                    canMove = False
                else:
                    if player[0] + 1 > roadList[roadIndex][0] + roadList[roadIndex][2]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False

        else:
            canMove = False
    return canMove


def colisaoRightCaminho2(player, road2List, roadIndex2):
    canMove = True
    caminhoSaida = [-1]

    if (player[0] + player[2]) + 1 >= road2List[roadIndex2][0] + road2List[roadIndex2][2]:
        if road2List[roadIndex2][4] != -1:
            for road in road2List[roadIndex2][4]:
                if road[0] == 3:
                    caminhoSaida = road
                    break

            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[1] and caminhoSaida[2] > player[1] + player[3]):
                    canMove = False
                else:
                    if player[0] + 1 > road2List[roadIndex2][0] + road2List[roadIndex2][2]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False

        else:
            canMove = False
    return canMove

def colisaoRightCaminho3(player, road3List, roadIndex3):
    canMove = True
    caminhoSaida = [-1]

    if (player[0] + player[2]) + 1 >= road3List[roadIndex3][0] + road3List[roadIndex3][2]:
        if road3List[roadIndex3][4] != -1:
            for road in road3List[roadIndex3][4]:
                if road[0] == 3:
                    caminhoSaida = road
                    break

            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[1] and caminhoSaida[2] > player[1] + player[3]):
                    canMove = False
                else:
                    if player[0] + 1 > road3List[roadIndex3][0] + road3List[roadIndex3][2]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False

        else:
            canMove = False
    return canMove


def colisaoLeftCaminho(player, roadList, roadIndex):
    canMove = True
    caminhoSaida = [-1]
    if player[0] - 1 <= roadList[roadIndex][0]:
        if roadList[roadIndex][4] != -1:
            for road in roadList[roadIndex][4]:

                if road[0] == 1:
                    caminhoSaida = road
                    break
            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[1] and caminhoSaida[2] > player[1] + player[3]):
                    canMove = False
                else:
                    if (player[0] + player[2]) - 1 > roadList[roadIndex][0]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False
        else:
            canMove = False

    return canMove

def colisaoLeftCaminho2(player, road2List, roadIndex2):
    canMove = True
    caminhoSaida = [-1]
    if player[0] - 1 <= road2List[roadIndex2][0]:
        if road2List[roadIndex2][4] != -1:
            for road in road2List[roadIndex2][4]:

                if road[0] == 1:
                    caminhoSaida = road
                    break
            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[1] and caminhoSaida[2] > player[1] + player[3]):
                    canMove = False
                else:
                    if (player[0] + player[2]) - 1 > road2List[roadIndex2][0]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False
        else:
            canMove = False

    return canMove

def colisaoLeftCaminho3(player, road3List, roadIndex3):
    canMove = True
    caminhoSaida = [-1]
    if player[0] - 1 <= road3List[roadIndex3][0]:
        if road3List[roadIndex3][4] != -1:
            for road in road3List[roadIndex3][4]:

                if road[0] == 1:
                    caminhoSaida = road
                    break
            if caminhoSaida[0] != -1:
                if not (caminhoSaida[1] < player[1] and caminhoSaida[2] > player[1] + player[3]):
                    canMove = False
                else:
                    if (player[0] + player[2]) - 1 > road3List[roadIndex3][0]:
                        print("Road antigo do player:", player[4])
                        player[4] = caminhoSaida[3]
                        print("Road novo do player:", player[4])
            else:
                canMove = False
        else:
            canMove = False

    return canMove


def executarMenu():
    btnJogar1 = pygame.image.load("imagens/btn_jogar_1.png")
    btnJogar2 = pygame.image.load("imagens/btn_jogar_2.png")
    btnSair1 = pygame.image.load("imagens/btn_sair_1.png")
    btnSair2 = pygame.image.load("imagens/btn_sair_2.png")
    btnComoJogar1 = pygame.image.load("imagens/ComoJogar1.png")
    btnComoJogar2 = pygame.image.load("imagens/ComoJogar2.png")
    btnSobre1 = pygame.image.load("imagens/Sobre1.png")
    btnSobre2 = pygame.image.load("imagens/Sobre2.png")

    recursos = {"btnJogar1": btnJogar1, "btnJogar2": btnJogar2, "btnSair1": btnSair1, "btnSair2": btnSair2}
    recursos2 = {"btnComoJogar1": btnComoJogar1, "btnComoJogar2": btnComoJogar2, "btnSobre1": btnSobre1, "btnSobre2": btnSobre2}

    sair = False
    btnJogarSel = False
    btnSairSel = False
    btnComoJogarSel = False
    btnSobreSel = False


    while not sair:

        for evento in pygame.event.get():

            if evento.type == pygame.MOUSEMOTION:
                if tela.get_size()[0] * 0.7 - btnJogar1.get_size()[0] * 0.7 <= evento.pos[0] <= tela.get_size()[0] * 0.7 + btnJogar1.get_size()[0] * 0.7:
                    if tela.get_size()[1] * 0.2 <= evento.pos[1] <= tela.get_size()[1] * 0.2 + btnJogar1.get_size()[1]:
                        btnJogarSel = True
                        btnSairSel = False
                        btnComoJogarSel = False
                        btnSobreSel = False
                    elif tela.get_size()[1] * 0.52 + btnJogar1.get_size()[1] <= evento.pos[1] <= tela.get_size()[1] * 0.5 + btnJogar1.get_size()[1] * 2:
                        btnJogarSel = False
                        btnSairSel = True
                        btnComoJogarSel = False
                        btnSobreSel = False
                    if tela.get_size()[0] * 0.7 - btnComoJogar1.get_size()[0] * 0.7 <= evento.pos[0] <= tela.get_size()[0] * 0.7 + btnComoJogar1.get_size()[0] * 0.7:
                        if tela.get_size()[1] * 0.39 <= evento.pos[1] <= tela.get_size()[1] * 0.39 + btnComoJogar1.get_size()[1]:
                            btnJogarSel = False
                            btnSairSel = False
                            btnComoJogarSel = True
                            btnSobreSel = False
                        elif tela.get_size()[1] * 0.3 + btnComoJogar1.get_size()[1] <= evento.pos[1] <= tela.get_size()[1] * 0.3 + btnComoJogar1.get_size()[1] * 2:
                            btnJogarSel = False
                            btnSairSel = False
                            btnComoJogarSel = False
                            btnSobreSel = True

                    else:
                        btnJogarSel = False
                        btnSairSel = False
                        btnComoJogarSel = False
                        btnSobreSel = False
                else:
                    btnJogarSel = False
                    btnSairSel = False
                    btnComoJogarSel = False
                    btnSobreSel = False

            if evento.type == pygame.MOUSEBUTTONUP:
                if btnSairSel:
                    sair = True
                if btnJogarSel:
                    ComoJogarFase1()
                    tela.blit(fase1, (0, 0))
                if btnComoJogarSel:
                    ExecutarComoJogar()
                if btnSobreSel:
                    ExecutarSobre()


        desenharMenu(recursos, btnJogarSel, btnSairSel, recursos2, btnComoJogarSel, btnSobreSel)

    if sair == True:
        pygame.display.quit()


def desenharMenu(recursos, btnJogarSel, btnSairSel, recursos2, btnComoJogarSel, btnSobreSel):
    tela.blit(menu, (0, 0))


    if btnJogarSel:
        tela.blit(recursos["btnJogar2"], (tela.get_size()[0] * 0.79 - recursos["btnJogar2"].get_size()[0] * 0.79, tela.get_size()[1] * 0.2))
    else:
        tela.blit(recursos["btnJogar1"], (tela.get_size()[0] * 0.79 - recursos["btnJogar2"].get_size()[0] * 0.79, tela.get_size()[1] * 0.2))

    if btnSairSel:
        tela.blit(recursos["btnSair2"], (tela.get_size()[0] * 0.66 - recursos["btnJogar2"].get_size()[0] * 0.01, tela.get_size()[1] * 0.5 + recursos["btnJogar2"].get_size()[1]))
    else:
        tela.blit(recursos["btnSair1"], (tela.get_size()[0] * 0.66 - recursos["btnJogar2"].get_size()[0] * 0.01, tela.get_size()[1] * 0.5 + recursos["btnJogar2"].get_size()[1]))

    if btnComoJogarSel:
        tela.blit(recursos2["btnComoJogar2"], (tela.get_size()[0] * 0.7 - recursos2["btnComoJogar2"].get_size()[0] * 0.45, tela.get_size()[1] * 0.35))
    else:
        tela.blit(recursos2["btnComoJogar1"], (tela.get_size()[0] * 0.7 - recursos2["btnComoJogar2"].get_size()[0] * 0.45, tela.get_size()[1] * 0.35))

    if btnSobreSel:
        tela.blit(recursos2["btnSobre2"], (tela.get_size()[0] * 0.67 - recursos2["btnComoJogar2"].get_size()[0] * 0.1, tela.get_size()[1] * 0.36 + recursos2["btnComoJogar2"].get_size()[1]))
    else:
        tela.blit(recursos2["btnSobre1"], (tela.get_size()[0] * 0.67 - recursos2["btnComoJogar2"].get_size()[0] * 0.1, tela.get_size()[1] * 0.36 + recursos2["btnComoJogar2"].get_size()[1]))

    tela.blit(click, (ret.left, ret.top))
    pygame.mouse.set_visible(False)
    (xant, yant) = (ret.left, ret.top)
    (ret.left, ret.top) = pygame.mouse.get_pos()
    ret.left -= ret.width / 2
    ret.top -= ret.width / 2

    pygame.display.flip()

def ExecutarComoJogar():
    gameover = False
    sair = False
    while not sair:
        tela.blit(comojogar_fundo, (0, 0))
        tela.blit(click, (ret.left, ret.top))
        pygame.mouse.set_visible(False)
        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                    gameover = True

        if gameover == True:
            executarMenu()

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()


def ExecutarSobre():
    gameover = False
    sair = False
    while not sair:
        tela.blit(sobre_fundo, (0, 0))
        tela.blit(click, (ret.left, ret.top))
        pygame.mouse.set_visible(False)
        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                gameover = True

        if gameover == True:
            executarMenu()

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()


sair = False

def ComoJogarFase1():
    sair = False

    while not sair:
        tela.blit(fase1, (0, 0))
        tela.blit(click, (ret.left, ret.top))
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                ExecutarFase1()

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()


def ComoJogarFase2():
    sair = False

    while not sair:
        tela.blit(fase2, (0, 0))
        tela.blit(click, (ret.left, ret.top))
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                ExecutarFase2()

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()

def ComoJogarFase3():
    sair = False

    while not sair:
        tela.blit(fase3, (0, 0))
        tela.blit(click, (ret.left, ret.top))
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                ExecutarFase3()

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()


def ExecutarFase1():
    jogador = [60, 180, 60, 60, 0]
    leftMove = upMove = rigthMove = downMove = False
    sair = False
    gameover = False
    ligar = True


    while not sair:
        pygame.draw.rect(tela, (0, 255, 0), road1[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road2[0:4])
        pygame.draw.rect(tela, (255, 0, 128), road3[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road4[0:4])
        pygame.draw.rect(tela, (13, 31, 255), road5[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road6[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road7[0:4])
        pygame.draw.rect(tela, (255, 0, 128), road8[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road9[0:4])
        pygame.draw.rect(tela, (255, 13, 13), road10[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road11[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road12[0:4])
        pygame.draw.rect(tela, (255, 0, 128), road13[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road14[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road15[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road16[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road17[0:4])
        pygame.draw.rect(tela, (255, 0, 128), road18[0:4])
        pygame.draw.rect(tela, (13, 31, 255), road19[0:4])
        pygame.draw.rect(tela, (255, 13, 13), road20[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road21[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road22[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road23[0:4])
        pygame.draw.rect(tela, (13, 31, 255), road24[0:4])
        pygame.draw.rect(tela, (255, 0, 128), road25[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road26[0:4])
        pygame.draw.rect(tela, (255, 13, 13), road27[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road28[0:4])
        pygame.draw.rect(tela, (13, 31, 255), road29[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road30[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road31[0:4])
        pygame.draw.rect(tela, (255, 13, 13), road32[0:4])
        pygame.draw.rect(tela, (255, 13, 13), buraco1[0:4])
        pygame.draw.rect(tela, (0, 255, 255), buraco2[0:4])
        pygame.draw.rect(tela, (255, 13, 13), casa[0:4])
        pygame.draw.rect(tela, (255, 13, 13), escada1[0:4])
        pygame.draw.rect(tela, (255, 13, 13), escada2[0:4])
        contorno = pygame.draw.rect(tela, (255, 0, 0), jogador[0:4])
        tela.blit(img_fundo, (0, 0))
        tela.blit(click, (ret.left, ret.top))

        if ligar == True:
            tela.blit(img_user1, (jogador[0], jogador[1]))

        if ligar == False:
            tela.blit(img_user2, (jogador[0], jogador[1]))

        if rigthMove or upMove or downMove == True:
            ligar = True
            tela.blit(img_user1, (jogador[0], jogador[1]))

        if leftMove == True:
            ligar = False
            tela.blit(img_user2, (jogador[0], jogador[1]))



        for event in pygame.event.get():
            if event.type == QUIT:
                sair = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    ComoJogarFase1()

                if event.key == K_UP:
                    upMove = True
                    leftMove = rigthMove = downMove = False

                if event.key == K_DOWN:
                    downMove = True
                    leftMove = upMove = rigthMove = False

                if event.key == K_LEFT:
                    tela.blit(img_user2, (jogador[0], jogador[1]))
                    leftMove = True
                    upMove = rigthMove = downMove = False

                if event.key == K_RIGHT:
                    rigthMove = True
                    tela.blit(img_user1, (jogador[0], jogador[1]))
                    leftMove = upMove = downMove = False

            if event.type == pygame.KEYUP:
                leftMove = upMove = rigthMove = downMove = False



        if contorno.colliderect(buraco1):
            jogador = [60, 180, 60, 60, 0]
            som_buraco.play()

        if contorno.colliderect(buraco2):
            jogador = [60, 180, 60, 60, 0]
            som_buraco.play()

        if contorno.colliderect(escada1):
            rigthMove = False
            som_escada.play()

        if contorno.colliderect(escada12):
            leftMove = False
            som_escada.play()

        if contorno.colliderect(escada2):
            rigthMove = False
            som_escada.play()

        if contorno.colliderect(escada22):
            leftMove = False
            som_escada.play()

        if contorno.colliderect(arvore1):
            rigthMove = False
            som_arvore.play()

        if contorno.colliderect(arvore12):
            leftMove = False
            som_arvore.play()

        if contorno.colliderect(arvore2):
            downMove = False
            som_arvore.play()

        if contorno.colliderect(arvore22):
            upMove = False
            som_arvore.play()



        if contorno.colliderect(casa):
            tela.blit(fim, (0, 0))
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    ComoJogarFase2()


        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2


        moverJogador(leftMove, upMove, rigthMove, downMove, jogador, roadList)

        if gameover == True:
            executarMenu()

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()



def ExecutarFase2():
    jogador = [100, 140, 60, 60, 0]
    leftMove = upMove = rigthMove = downMove = False
    sair = False
    gameover = False
    ligar = True


    while not sair:
        tela.blit(img_fundo2, (0, 0))
        contorno = pygame.draw.rect(tela, (255, 0, 0), jogador[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road01[0:4])
        pygame.draw.rect(tela, (255, 255, 0), road02[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road03[0:4])
        pygame.draw.rect(tela, (255, 255, 255), road04[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road05[0:4])
        pygame.draw.rect(tela, (255, 255, 0), road06[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road07[0:4])
        pygame.draw.rect(tela, (0, 0, 255), road08[0:4])
        pygame.draw.rect(tela, (255, 0, 255), road09[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road010[0:4])
        pygame.draw.rect(tela, (255, 255, 0), road011[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road012[0:4])
        pygame.draw.rect(tela, (255, 0, 0), road013[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road014[0:4])
        pygame.draw.rect(tela, (255, 255, 255), road015[0:4])
        pygame.draw.rect(tela, (255, 255, 0), road016[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road017[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road018[0:4])
        pygame.draw.rect(tela, (255, 255, 0), road019[0:4])
        pygame.draw.rect(tela, (255, 255, 255), road020[0:4])
        pygame.draw.rect(tela, (255, 13, 13), buraco3[0:4])
        pygame.draw.rect(tela, (0, 255, 255), buraco4[0:4])
        tela.blit(img_fundo2, (0, 0))
        tela.blit(click, (ret.left, ret.top))

        if ligar == True:
            tela.blit(img_user3, (jogador[0], jogador[1]))

        if ligar == False:
            tela.blit(img_user4, (jogador[0], jogador[1]))

        if rigthMove or upMove or downMove == True:
            ligar = True
            tela.blit(img_user3, (jogador[0], jogador[1]))

        if leftMove == True:
            ligar = False
            tela.blit(img_user4, (jogador[0], jogador[1]))

        for event in pygame.event.get():

            if event.type == QUIT:
                sair = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    ComoJogarFase2()

                if event.key == K_UP:
                    upMove = True
                    leftMove = rigthMove = downMove = False

                if event.key == K_DOWN:
                    downMove = True
                    leftMove = upMove = rigthMove = False

                if event.key == K_LEFT:
                    leftMove = True
                    upMove = rigthMove = downMove = False

                if event.key == K_RIGHT:
                    rigthMove = True
                    leftMove = upMove = downMove = False

            if event.type == pygame.KEYUP:
                leftMove = upMove = rigthMove = downMove = False

                for event in pygame.event.get():
                    if (event.type == pygame.KEYDOWN):
                        gameover = True


        if contorno.colliderect(buraco3):
            jogador = [100, 140, 60, 60, 0]
            som_buraco.play()

        if contorno.colliderect(buraco4):
            jogador = [100, 140, 60, 60, 0]
            som_buraco.play()

        if contorno.colliderect(lixo1):
            downMove = False
            som_lixo.play()

        if contorno.colliderect(lixo12):
            upMove = False
            som_lixo.play()

        if contorno.colliderect(lixo2):
            rigthMove = False
            leftMove = True
            som_lixo.play()

        if contorno.colliderect(lixo22):
            leftMove = False
            rigthMove = True
            som_lixo.play()


        if contorno.colliderect(casa2):
            tela.blit(fim, (0, 0))
            #aplausos.play()
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    ComoJogarFase3()

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2


        moverJogador2(leftMove, upMove, rigthMove, downMove, jogador, road2List)


        if gameover == True:
            executarMenu()

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()

def ExecutarFase3():
    jogador = [140, 150, 50, 60, 0]
    leftMove = upMove = rigthMove = downMove = False
    sair = False
    gameover = False
    ligar = True


    while not sair:
        pygame.draw.rect(tela, (0, 255, 0), road001[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road002[0:4])
        pygame.draw.rect(tela, (255, 0, 128), road003[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road004[0:4])
        pygame.draw.rect(tela, (13, 31, 255), road005[0:4])
        pygame.draw.rect(tela, (0, 255, 0), road006[0:4])
        pygame.draw.rect(tela, (0, 64, 128), road007[0:4])
        pygame.draw.rect(tela, (255, 0, 128), road008[0:4])
        pygame.draw.rect(tela, (0, 255, 255), road009[0:4])
        pygame.draw.rect(tela, (255, 13, 13), road0010[0:4])
        pygame.draw.rect(tela, (255, 13, 13), road0011[0:4])
        contorno = pygame.draw.rect(tela, (255, 0, 0), jogador[0:4])
        tela.blit(img_fundo3, (0, 0))
        tela.blit(click, (ret.left, ret.top))

        if ligar == True:
            tela.blit(img_user5, (jogador[0], jogador[1]))

        if ligar == False:
            tela.blit(img_user6, (jogador[0], jogador[1]))

        if rigthMove or upMove or downMove == True:
            ligar = True
            tela.blit(img_user5, (jogador[0], jogador[1]))

        if leftMove == True:
            ligar = False
            tela.blit(img_user6, (jogador[0], jogador[1]))


        for event in pygame.event.get():
            if event.type == QUIT:
                sair = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    ComoJogarFase3()

                if event.key == K_UP:
                    upMove = True
                    leftMove = rigthMove = downMove = False

                if event.key == K_DOWN:
                    downMove = True
                    leftMove = upMove = rigthMove = False

                if event.key == K_LEFT:
                    leftMove = True
                    upMove = rigthMove = downMove = False

                if event.key == K_RIGHT:
                    rigthMove = True
                    leftMove = upMove = downMove = False

            if event.type == pygame.KEYUP:
                leftMove = upMove = rigthMove = downMove = False


        if contorno.colliderect(escola1):
            rigthMove = False
            leftMove = True
            som_libras1.play()

        if contorno.colliderect(escola2):
            som_libras2.play()
            executarFim()


        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2


        moverJogador3(leftMove, upMove, rigthMove, downMove, jogador, road3List)

        if gameover == True:
            executarMenu()

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()


def executarFim():
    sair = False
    gameover = False
    tela.blit(final, (0, 0))

    while not sair:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                executarMenu()

        if gameover == True:
            executarMenu()

        if not sair:
            pygame.display.flip()
        else:
            pygame.display.quit()


if sair == True:
    pygame.display.quit()

executarMenu()