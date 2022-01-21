import pygame
from pygame.locals import *
# inicia pygame
pygame.init()

########################################################
"""     Variáveis ou atributos      """
#minhas variáveis
backgroud = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)

playerMedidas = [50, 50, 50, 50] # [X, Y, Tamanho_X, Tamanho_Y]
click = pygame.image.load("imagens/click1.png").convert_alpha()
ret = pygame.Rect(5, 5, 50, 50)
img_fundo = pygame.image.load("imagens/fundo3.png").convert_alpha()

objetoMedidas = [200, 200, 300, 100] # [X, Y, Tamanho_X, Tamanho_Y]
jogar = [1200, 210, 370, 130]
comojogar = [1060, 400, 660, 130]
sobre = [1200, 580, 370, 130]
sair = [1270, 750, 230, 130]



########################################################
"""     funções ou ações do jogo    """
def movePlayer(left, up, rigth, down, player, object):
    if left and collisionLeft(player, object):
        player[0] -= 10
    if up and collisionUP(player, object):
        player[1] -= 10
    if rigth and collisionRight(player, object):
        player[0] += 10
    if down and collisionDown(player, object):
        player[1] += 10

def collisionDown(player, object):
    #Variável que retorna se pode ou não mover
    canMove = True

    # verifico se está dentro da mesma coluna que o obstáculo
    if object[0] < player[0]+player[2] and object[0]+object[2] > player[0]:
        #verifico se já está abaixo do obstáculo
        if not object[1] + object[3] < player[1]:
            # verificando se o próximo passo irá colidir com o objeto
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

	# verificando se o player está dentro da mesma linha que o objeto
	if (object[1] < player[1]+player[3] and object[1]+object[3] > player[1]):
		print("mesma linha do objeto")
		# verificando se já está a esquerda do objeto
		if not player[0] > object[0] + object[2]:
			print("está a esquerda do objeto")
			if (player[0]+player[2])+1 >= object[0]:
				print("colidiu")
				canMove = False

	return canMove

def collisionLeft(player, object):
	canMove = True

	# verificando se o player está dentro da mesma linha que o objeto
	if (object[1] < player[1]+player[3] and object[1]+object[3] > player[1]):
		print("mesma linha do objeto")
		# verificando se já está a esquerda do objeto
		if not player[0] + player[2] < object[0]:
			print("está a direita do objeto")
			if player[0]-1 <= object[0]+object[2]:
				print("colidiu")
				canMove = False

	return canMove

########################################################
"""     MAIN                    """

leftMove = upMove = rigthMove = downMove = False
gameOver = False
menu = pygame.image.load("imagens/menu.png").convert_alpha()
backgroud.blit(menu, (0, 0))

while not gameOver:
    pygame.draw.rect(backgroud, (255,255,0), playerMedidas)
    pygame.draw.rect(backgroud, (255,0,0), objetoMedidas)
    pygame.draw.rect(backgroud, (0,0,0), jogar)
    pygame.draw.rect(backgroud, (0,0,0), comojogar)
    pygame.draw.rect(backgroud, (0,0,0), sobre)
    pygame.draw.rect(backgroud, (0,0,0), sair)


    """ caso tenha uma imagem para o seu obejto e seu player """
    # backgroud.blit(playerSuface, (playerMedidas[0], playerMedidas[1]))
    # backgroud.blit(objSuface, (objetoMedidas[0], objetoMedidas[1]))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            backgroud.blit(img_fundo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

        if event.type == pygame.KEYDOWN:
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

            if event.key == K_ESCAPE:
                gameOver = True

        if event.type == pygame.KEYUP:
            leftMove = upMove = rigthMove = downMove = False

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.width / 2

    movePlayer(leftMove, upMove, rigthMove, downMove, playerMedidas, objetoMedidas)


    #fim de jogo
    if not gameOver:
        pygame.display.flip()
    else:
        pygame.display.quit()
