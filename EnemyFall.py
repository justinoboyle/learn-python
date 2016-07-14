import pygame
import random
import config

class EnemyFall(pygame.sprite.Sprite):

    texts = [ "spider", "bug" ]

    def __init__(self):
        global texts
        super().__init__()
        
        self.image = pygame.image.load("res/images/enemy/" + self.texts[random.randint(0, len(self.texts) - 1)] + ".png").convert_alpha()
        self.rect = self.image.get_rect(center=(40, 40))
        self.rect.x = random.randint(0, config.game_width - 40)
        self.rect.y = -10

    def update(self):
        if random.randint(0, 3) == 1:
            self.rect.x += random.choice([-1, 1]) * 3
        self.rect.y += 5