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

    lives = 3
    score = 0

    def init(self, screen):

        self.centipedes = []
        self.background = None
        self.collideWith = pygame.sprite.Group()
        self.mushroom_group = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.split = False
        self.time = 0
        self.screen = screen

        self.background = pygame.Surface((0, 0), 0, screen)
        self.background.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))
        self.centipedes.append(Centipede(self))
        time = pygame.time.get_ticks()
        self.players.add(Player())
        for i in range(20, 40):
            self.mushroom_group.add(Mushroom(random.randint(0, config.game_width - 20), random.randint(60, config.game_height - 120)))
        self.myfont = pygame.font.SysFont("monospace", 12)
        self.largefont = pygame.font.SysFont("monospace", 20)

    def emitSpaceBar(self):
        if self.lives <= 0:
            self.lives = 3
            self.score = 0
            self.init(self.screen)
            return
        self.bullets.add(Bullet(self.players.sprites()[0].rect.x, self.players.sprites()[0].rect.y))

    def emit(self, screen):
        if self.lives <= 0:
            screen.blit(self.largefont.render("You died! Press space to replay.", 1, (255, 255, 255)), (config.game_width / 2 - 190, config.game_height / 2 - 8))
            screen.blit(self.largefont.render("Score: " + str(self.score), 1, (255, 255, 255)), (config.game_width / 2 - 190, config.game_height / 2 + 8))
            return
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
            for part in centipede.centipede_group:
                if part.rect.y > config.game_height - 120:
                    self.lives -= 1
                    self.init(screen)
                    return
            centipede.update(screen, self.background, self.mushroom_group, self.bullets)
            count += 1
Controller()