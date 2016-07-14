import pygame
import config
from CentipedeComponent import CentipedeComponent
from Centipede import Centipede
from Mushroom import Mushroom
import time 
import random
from Player import Player
from Bullet import Bullet
from EnemyFall import EnemyFall

class Controller():

    lives = 3
    score = 0

    def init(self, screen):
        pygame.display.set_caption("Centipede")
        self.difficulty = 1
        self.difficultyTimer = pygame.time.get_ticks()
        self.centipedes = []
        self.background = None
        self.collideWith = pygame.sprite.Group()
        self.mushroom_group = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
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

        if random.randint(0, 1000 - (self.difficulty * 10)) < 5:
            self.enemies.add(EnemyFall())

        if pygame.time.get_ticks() - self.difficultyTimer >= 5 * 1000:
            self.difficulty += 1
            self.difficultyTimer = pygame.time.get_ticks()
        
        

        self.players.draw(screen)
        self.bullets.draw(screen)
        self.mushroom_group.draw(screen)
        self.enemies.draw(screen)
        count = 0

        screen.blit(self.myfont.render("Lives:", 1, (255, 255, 255)), (60, 10))
        screen.blit(self.myfont.render(str(self.lives), 1, (255, 255, 255)), (60, 20))
        screen.blit(self.myfont.render("Score:", 1, (255, 255, 255)), (config.game_width - 120, 10))
        screen.blit(self.myfont.render(str(self.score), 1, (255, 255, 255)), (config.game_width - 120, 20))

        for player in self.players:
            if player.update(self.enemies):
                self.lives -= 1
                score = self.score
                self.init(screen)
                self.score = score
                return

        if len(self.centipedes) <= 0:
            self.centipedes.append(Centipede(self))

        for bullet in self.bullets:
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
            else:
                bullet.update()

        for enemy in self.enemies:
            if enemy.rect.y > config.game_height:
                self.enemies.remove(enemy)
            else:
                enemy.update()

        for centipede in self.centipedes:
            for part in centipede.centipede_group:
                if part.rect.y > config.game_height - 120:
                    self.lives -= 1
                    score = self.score
                    self.init(screen)
                    self.score = score
                    return
            centipede.update(screen, self.background, self.mushroom_group, self.bullets)
            count += 1

Controller()