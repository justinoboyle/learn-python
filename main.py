import config
import pygame
import random
import math
import sys
from pygame.locals import *
import time
import game_controller
import event

game_clock = pygame.time.Clock()

delta_time = 1

pygame.init()
screen = pygame.display.set_mode((config.game_width, config.game_height))

pygame.key.set_repeat(100, 50)

font = pygame.font.SysFont(None, 36)

game_run = True

game_controller.init()

def msTime():
    return int(time.time() * 1000)

def draw():
    game_clock.tick(config.game_sync_framerate)
    screen.fill((0, 0, 0))
    game_controller.emitUpdateObjects(delta_time)
    game_controller.emit(screen)
    pygame.display.update()

def checkEvents():
    for event in events:
        if event.type == QUIT:
            game_run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_controller.emitSpaceBar()

while game_run:
    startRender = msTime()
    checkEvents()
    draw()
    DELTA_TIME = 1.0 - (1 / (msTime() - startRender))

pygame.quit()
sys.exit()