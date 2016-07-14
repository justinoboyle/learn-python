import pygame
import config

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.bullets = pygame.sprite.Group()
        self.image = pygame.image.load("res/images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(19, 19))
        self.rect.x = (config.game_width / 2)
        self.rect.y = config.game_height - 20

    def update(self, enemies):
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        if pos[1] < config.game_height - 120:
            pygame.mouse.set_visible(True)
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = max(pygame.mouse.get_pos()[1], config.game_height - 120)
        return self.check(enemies)

    def check(self, enemies):
        return len(pygame.sprite.spritecollide(self, enemies, True)) > 0
    
    def fire(self):
        print("Fire!")