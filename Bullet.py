import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("res/images/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=(5, 10))
        self.rect.x = x
        self.rect.y = y + 15

    def update(self):
        self.rect.y -= 5