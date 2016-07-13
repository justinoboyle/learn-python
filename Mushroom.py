import pygame

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("res/images/mushroom.png").convert_alpha()
        self.rect = self.image.get_rect(center=(20, 20))
        self.rect.x = x
        self.rect.y = y