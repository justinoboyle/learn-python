import pygame
import config
from Direction import Direction

def swapDirection(dir, lasthor):
    if dir == Direction.up: return Direction.right if lasthor == Direction.left else Direction.left
    elif dir == Direction.right: return Direction.down
    elif dir == Direction.down: return Direction.right if lasthor == Direction.left else Direction.left
    elif dir == Direction.left: return Direction.down

class CentipedeComponent(pygame.sprite.Sprite):

    def __init__(self, parentObj):
        super().__init__()

        self.currentImage = None

        self.direction = Direction.right

        self.parent = None

        self.rotateAgain = -1
        self.rotateTimer = -1

        self.updateDirection()

        self.parent = parentObj
        self.setCurrentImage("body_up")
        self.rect = self.image.get_rect(center=(self.getDim(), self.getDim()))
        
    def getActiveImage(self):
        return currentImage

    def setCurrentImage(self, image):
        if image == self.currentImage:
            return # Don't change it if it's already the same
        currentImage = "res/images/cent/" + image + ".png"
        self.image = pygame.image.load(currentImage).convert_alpha()

    def collide(self, collideWith, bullets, selfX, selfY, index):

        bull = pygame.sprite.spritecollide(self, bullets, True)
        if len(bull) > 0:
            self.parent.divide(index)
            self.parent.controller.score += 10
            return swapDirection(self.direction, self.lasthor)

        if selfY <= 0 and self.direction != swapDirection(Direction.up, self.lasthor):
            return swapDirection(Direction.up, self.lasthor)
        if selfX <= 0 and self.direction != swapDirection(Direction.left, self.lasthor):
            return swapDirection(Direction.left, self.lasthor)
        if (selfY + self.getDim()) >= config.game_height and self.direction != swapDirection(Direction.down, self.lasthor):
            return swapDirection(Direction.right, self.lasthor)
        if (selfX + self.getDim()) >= config.game_width and self.direction != swapDirection(Direction.right, self.lasthor):
            return swapDirection(Direction.right, self.lasthor)
        coll = pygame.sprite.spritecollide(self, collideWith, False)
        if len(coll) > 0:
            for x in coll:
                rect = x.image.get_rect()
                if rect.x > self.rect.x:
                    return swapDirection(Direction.left, self.lasthor)
                if rect.x < self.rect.x:
                    return swapDirection(Direction.right, self.lasthor)
                if rect.y < self.rect.y:
                    return swapDirection(Direction.right, self.lasthor)

            return swapDirection(Direction.up, self.lasthor)
        return Direction.none

    def move(self, headX, headY, isHead, amount, collideWith, bullets, index, headIndex, centipede_group):
        head = centipede_group.sprites()[headIndex]
        if self.rotateAgain != -1:
            if pygame.time.get_ticks() - self.rotateTimer >= self.rotateAgain:
                self.direction = swapDirection(self.direction, self.lasthor)
                self.updateDirection()
                self.rotateAgain = -1
                self.rotateTimer = -1
            

        if self.direction == Direction.up: self.rect.y -= amount
        elif self.direction == Direction.right: self.rect.x += amount
        elif self.direction == Direction.down: self.rect.y += amount
        elif self.direction == Direction.left: self.rect.x -= amount

        collide = self.collide(collideWith, bullets, self.rect.x, self.rect.y, index)
        if collide != Direction.none:
            self.direction = collide
            self.updateDirection()
            self.rotateAgain = 250
            self.rotateTimer = pygame.time.get_ticks()

        self.setCurrentImage(("head" if isHead else "body") + "_" + self.direction.value)
    def distanceTo(self, other):
        return pow(pow(other.rect.x - self.rect.x, 2) + pow(other.rect.y - self.rect.y, 2), 0.5)

    def getDim(self):
        return 20 # TODO make this dynamic

    def updateDirection(self):
        if self.direction == Direction.right or self.direction == Direction.left:
            self.lasthor = self.direction