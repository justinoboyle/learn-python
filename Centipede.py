import pygame
import config
from CentipedeComponent import CentipedeComponent
from Direction import Direction

def backwards(dir):
    if dir == Direction.up: return Direction.down
    elif dir == Direction.right: return Direction.left
    elif dir == Direction.down: return Direction.up
    elif dir == Direction.left: return Direction.left

class Centipede():

    def __init__(self, controller, initAmount = 10, initX = 20 + (5 * 10), initY = 20, initMove = 0):

        self.centipede_group = pygame.sprite.Group()
        self.moveAmount = initMove
        self.facingRight = True
        self.speed = 1
        self.controller = None

        print("initAmount: " + str(initAmount))
        self.controller = controller
        self.headX = initX
        self.headY = initY
        if initAmount > 0:
            for x in range(0, initAmount):
                self.centipede_group.add(CentipedeComponent(self))
            self.initPos()

    def update(self, screen, background, collideWith, bullets):
        self.updatePos(collideWith, bullets)
        self.centipede_group.draw(screen)

    def divide(self, at):
        atX = self.centipede_group.sprites()[at].rect.x
        atY = self.centipede_group.sprites()[at].rect.y
        amount = at
        for x in range(at, len(self.centipede_group.sprites())):
            obj = self.centipede_group.sprites()[x]
            self.centipede_group.sprites().remove(obj)
        if len(self.centipede_group) < 2:
            self.controller.centipedes.remove(self)
        if amount < 2:
            return None
        temp = Centipede(self.controller, amount, atX, atY, self.moveAmount)
        for x in temp.centipede_group:
            x.direction = backwards(x.direction)
            x.updateDirection()
        self.controller.centipedes.append(temp)
        print("Break")


    def initPos(self):
        count = 0
        for x in self.centipede_group:
            x.rect.x = self.headX + (20 * count)
            x.rect.y = self.headY + 20
            count += 1

    def updatePos(self, collideWith, bullets):
        count = 0
        for trail in self.centipede_group:
            trail.move(self.headX, self.headY, count == len(self.centipede_group) -1, 2, collideWith, bullets, count, len(self.centipede_group) - 1, self.centipede_group)
            count += 1