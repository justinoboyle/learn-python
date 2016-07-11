import pygame
import config

hoop_image = None
arrow_image = None
ball_image = None

hoopDim = int(config.game_width / 5)
hoopMod = 0
hoopMax = config.game_width - hoopDim
hoopDir = 1

arrowDim = int(config.game_width / 10)

ballDim = int(config.game_height / 15)
ballStartHeight = arrowDim
ballLaunched = False
ballHeight = ballStartHeight

def init():
    global hoop_image, arrow_image, ball_image

    hoop_image = pygame.image.load('res/images/hoop.png').convert_alpha()
    hoop_image = pygame.transform.scale(hoop_image, (hoopDim, hoopDim))

    arrow_image = pygame.image.load('res/images/arrow.png').convert_alpha()
    arrow_image = pygame.transform.scale(arrow_image, (arrowDim, arrowDim))

    ball_image = pygame.image.load('res/images/ball.png').convert_alpha()
    ball_image = pygame.transform.scale(ball_image, (ballDim, ballDim))

def emit(screen):
    updateBall()
    screen.blit(hoop_image, (hoopMod, config.game_height - hoopDim))
    screen.blit(arrow_image, ((config.game_width / 2) - arrowDim, 0))
    if ballLaunched:
        screen.blit(ball_image, (((config.game_width / 2) - arrowDim) + (ballDim / 2), ballStartHeight))

def updateBall(deltaTime):
    if not ballLaunched:
        return

#def emitUpdateObjects(delta_time):
#TODO

def emitSpaceBar():
    if ballLaunched:
        return
    ballHeight = ballStartHeight
    ballLaunched = True

def renderText(display, font, surface, x, y):
    text = font.render(display, 1, (0, 0, 0))
    surface.blit(text, (x, y))