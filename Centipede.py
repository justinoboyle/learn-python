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

    centipede_group = pygame.sprite.Group()
    moveAmount = 0
    facingRight = True
    headX = 20 + (5 * 10)
    headY = 20
    speed = 1
    controller = None

    def __init__(self, controller, initAmount = 10, initX = 20 + (5 * 10), initY = 20):
        global centipede_group
        self.controller = controller
        self.headX = initX
        self.headY = initY
        if initAmount > 0:
            for x in range(0, initAmount):
                self.centipede_group.add(CentipedeComponent(self))
        self.initPos()

    def update(self, screen, background, collideWith, bullets):
        self.updatePos(collideWith, bullets)
        self.centipede_group.clear(screen, background)
        self.centipede_group.draw(screen)

    def split(self, at):
        atObj = self.centipede_group.sprites()[at]
        temp = Centipede(self.controller, len(self.centipede_group) - 1 - at, atObj.rect.x, atObj.rect.y)
        x = 0
        for obj in self.centipede_group:
            if x < at:
                x += 1
                continue
            self.centipede_group.remove(obj)
            x += 1
        for x in temp.centipede_group:
            x.direction = backwards(x.direction)
        temp.initPos()
        return temp #LEFT OFF here


    def initPos(self):
        count = 0
        for x in self.centipede_group:
            x.rect.x = self.headX + (20 * count)
            x.rect.y = self.headY
            count += 1

    def updatePos(self, collideWith, bullets):
        global headX, headY
        count = 0
        for trail in self.centipede_group:
            trail.move(self.headX, self.headY, count == len(self.centipede_group) -1, 0.01, collideWith, bullets, count)
            count += 1