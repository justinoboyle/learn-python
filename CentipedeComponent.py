import pygame
import config
from Direction import Direction


def swapDirection(dir):
    if dir == Direction.up: return Direction.right
    elif dir == Direction.right: return Direction.down
    elif dir == Direction.down: return Direction.left
    elif dir == Direction.left: return Direction.up

class CentipedeComponent(pygame.sprite.Sprite):

    currentImage = None

    direction = Direction.right

    parent = None

    def __init__(self, parentObj):
        super().__init__()
        self.parent = parentObj
        self.setCurrentImage("body_up")
        self.rect = self.image.get_rect(center=(self.getDim(), self.getDim()))
        
    def getActiveImage(self):
        return currentImage

    def setCurrentImage(self, image):
        global currentImage
        if image == self.currentImage:
            return # Don't change it if it's already the same
        currentImage = "res/images/cent/" + image + ".png"
        self.image = pygame.image.load(currentImage).convert_alpha()

    def collide(self, collideWith, bullets, selfX, selfY, index):

        bull = pygame.sprite.spritecollide(self, bullets, True)
        if len(bull) > 0:
            self.parent.split(index)
            return self.direction

        if selfY <= 0 and self.direction != swapDirection(Direction.up):
            return Direction.up
        if selfX <= 0 and self.direction != swapDirection(Direction.left):
            return Direction.left
        if (selfY + self.getDim()) >= config.game_height and self.direction != swapDirection(Direction.down):
            return Direction.down
        if (selfX + self.getDim()) >= config.game_width and self.direction != swapDirection(Direction.right):
            return Direction.right
        coll = pygame.sprite.spritecollide(self, collideWith, False)
        if len(coll) > 0:
            return self.direction
        return Direction.none

    def move(self, headX, headY, isHead, amount, collideWith, bullets, index):
        global rect

        if self.direction == Direction.up: self.rect.y -= amount
        elif self.direction == Direction.right: self.rect.x += amount
        elif self.direction == Direction.down: self.rect.y += amount
        elif self.direction == Direction.left: self.rect.x -= amount

        collide = self.collide(collideWith, bullets, self.rect.x, self.rect.y, index)
        if collide != Direction.none:
            self.direction = swapDirection(collide)

        self.setCurrentImage(("head" if isHead else "body") + "_" + self.direction.value)

    def getDim(self):
        return 20 # TODO make this dynamic