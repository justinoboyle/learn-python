import pygame
import config
from CentipedeComponent import CentipedeComponent
from Centipede import Centipede
class Controller():
    centipedes = []

    background = None

    collideWith = pygame.sprite.Group()

    bullets = pygame.sprite.Group()

    def init(self, screen):
        global background, centipede
        self.background = pygame.Surface((640, 460), 0, screen)
        self.background.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))
        self.centipedes.append(Centipede(self))
        self.centipedes.append(self.centipedes[0].split(5))

    def emit(self, screen):
        count = 0
        for centipede in self.centipedes:
            print()
            centipede.update(screen, self.background, self.collideWith, self.bullets)
Controller()