import sys
import pygame
from pygame.locals import *

def emit(events):
    for event in events:
        if event.type == QUIT:
            game_run = False
            pygame.quit()
            sys.exit()