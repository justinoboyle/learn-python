import config
import pygame
import random
import math
import sys
from pygame.locals import *
import time
import game_render
import event

game_clock = pygame.time.Clock()

delta_time = 1

pygame.init()
screen = pygame.display.set_mode((config.game_width, config.game_height))

pygame.key.set_repeat(100, 50)

font = pygame.font.SysFont(None, 36)

game_run = True

def renderText(display, font, surface, x, y):
    text = font.render(display, 1, (0, 0, 0))
    surface.blit(text, (x, y))

def msTime():
    return int(time.time() * 1000)

def draw():
    game_clock.tick(config.game_sync_framerate)
    screen.fill((0, 0, 0))
    game_render.emit()
    pygame.display.update()

def checkEvents():
    event.emit(pygame.event.get())

while game_run:
    startRender = msTime()
    checkEvents()
    draw()
    DELTA_TIME = 1.0 - (1 / (msTime() - startRender))

pygame.quit()
sys.exit()