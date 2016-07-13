import pygame
import config
from CentipedeComponent import CentipedeComponent
from Centipede import Centipede
from Mushroom import Mushroom
import time 
import random
from Player import Player
from Bullet import Bullet

class Controller():
    centipedes = []

    background = None

    lives = 3

    score = 0

    collideWith = pygame.sprite.Group()

    mushroom_group = pygame.sprite.Group()

    bullets = pygame.sprite.Group()

    players = pygame.sprite.Group()

    split = False

    time = 0

    def init(self, screen):
        self.background = pygame.Surface((0, 0), 0, screen)
        self.background.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))
        self.centipedes.append(Centipede(self))
        time = pygame.time.get_ticks()
        self.players.add(Player())
        for i in range(20, 40):
            self.mushroom_group.add(Mushroom(random.randint(0, config.game_width - 20), random.randint(60, config.game_height - 120)))
        self.myfont = pygame.font.SysFont("monospace", 12)

    def emitSpaceBar(self):
        self.bullets.add(Bullet(self.players.sprites()[0].rect.x, self.players.sprites()[0].rect.y))

    def emit(self, screen):
        #do this
        self.mushroom_group.draw(screen)
        for player in self.players:
            player.update()
        for bullet in self.bullets:
            bullet.update()
        self.players.draw(screen)
        self.bullets.draw(screen)
        count = 0
        # render text
        screen.blit(self.myfont.render("Lives:", 1, (255, 255, 255)), (60, 10))
        screen.blit(self.myfont.render(str(self.lives), 1, (255, 255, 255)), (60, 20))
        screen.blit(self.myfont.render("Score:", 1, (255, 255, 255)), (config.game_width - 120, 10))
        screen.blit(self.myfont.render(str(self.score), 1, (255, 255, 255)), (config.game_width - 120, 20))
        for centipede in self.centipedes:
            # if not self.split and (pygame.time.get_ticks() - self.time) > 1000 * 5:
            #     self.centipedes.append(self.centipedes[0].divide(5))
            #     self.split = True 
            centipede.update(screen, self.background, self.mushroom_group, self.bullets)
            count += 1
Controller()