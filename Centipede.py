import pygame
import config
from CentipedeComponent import CentipedeComponent
from Direction import Direction
from threading import Timer
from PendingMovement import PendingMovement

def backwards(dir):
    if dir == Direction.up: return Direction.down
    elif dir == Direction.right: return Direction.left
    elif dir == Direction.down: return Direction.up
    elif dir == Direction.left: return Direction.left

class Centipede():

    def __init__(self, controller, initAmount = 10, initX = 20 + (5 * 10), initY = 20, initMove = 0, newG = pygame.sprite.Group()):

        self.centipede_group = newG
        self.moveAmount = initMove
        self.facingRight = True
        self.speed = 2
        self.controller = None

        self.pendingMovements = []

        print("initAmount: " + str(initAmount))
        self.controller = controller
        self.headX = initX
        self.headY = initY
        if initAmount > 0:
            for x in range(0, initAmount):
                self.centipede_group.add(CentipedeComponent(self))
            if initX > 0:
           	    self.initPos()

    def update(self, screen, background, collideWith, bullets):
        self.updatePos(collideWith, bullets)
        self.centipede_group.draw(screen)

    def divide(self, at):  
        try:
            origLen = len(self.centipede_group)
            if origLen == 0:
                return
            atX = self.centipede_group.sprites()[at].rect.x
            atY = self.centipede_group.sprites()[at].rect.y
            rem = 0
            newG = pygame.sprite.Group()
            while len(self.centipede_group) >= at and len(self.centipede_group) >= 1:
                obj = self.centipede_group.sprites()[len(self.centipede_group.sprites()) - 1]
                rem += 1
                if rem != 0:
                    newG.add(obj)
                self.centipede_group.remove(obj)
            if len(self.centipede_group) <= 1:
                self.controller.centipedes.remove(self)
            if len(newG) <= 2:
                return
            temp = Centipede(self.controller, 0, -1, -1, self.moveAmount, newG)
            for x in temp.centipede_group:
                x.parent = temp
                x.direction = backwards(x.direction)
                x.updateDirection()
            self.controller.centipedes.append(temp)
        except Exception as e:
            print(e.message)


    def initPos(self):
        count = 0
        for x in self.centipede_group:
            x.rect.x = self.headX + (20 * count)
            x.rect.y = self.headY + 20
            count += 1

    def updatePos(self, collideWith, bullets):
        count = 0
        direction = None
        newX = 0
        newY = 0
        trail = self.centipede_group.sprites()[len(self.centipede_group.sprites()) - 1]
        trail.move(self.headX, self.headY, self.speed, collideWith, bullets, count, self.centipede_group)
        direction = trail.direction
        newX = trail.rect.x
        newY = trail.rect.y
        self.pendingMovements.append(PendingMovement((7 / 2) * self.speed, self.centipede_group, newX, newY, collideWith, bullets, trail.direction))
        for m in self.pendingMovements:
            if m.tick():
                self.pendingMovements.remove(m)