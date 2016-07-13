import config
import pygame
import random
import math
import sys
from pygame.locals import *
import timex
from game_controller import Controller
import event
import os

x = 50
y = 50

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

controllerObj = Controller()

game_clock = pygame.time.Clock()

delta_time = 1

pygame.init()
screen = pygame.display.set_mode((config.game_width, config.game_height))

pygame.key.set_repeat(100, 50)

game_run = True

font = pygame.font.SysFont(None, 36)

def msTime():
    return int(time.time() * 1000)

def draw():
    game_clock.tick(config.game_sync_framerate)
    screen.fill((0, 0, 0))
    # controllerObj.emitUpdateObjects(delta_time)
    controllerObj.emit(screen)
    pygame.display.update()

def checkEvents(events):
    for event in events:
        if event.type == QUIT:
            game_run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                controllerObj.emitSpaceBar()

controllerObj.init(screen)

while game_run:
    startRender = msTime()
    checkEvents(pygame.event.get())
    draw()
    DELTA_TIME = 1.0 - (1 / (msTime() - startRender))

pygame.quit()
sys.exit()