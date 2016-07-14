class PendingMovement():

    def __init__(self, runIn, parts, x, y, collideWith, bullets, direction):
        self.runIn = runIn
        self.parts = parts
        self.x = x
        self.y = y
        self.collideWith = collideWith
        self.bullets = bullets
        self.direction = direction
        self.mark = len(parts) - 1
        self.ticks = 0
    
    def tick(self):
        if self.ticks < self.runIn:
            self.ticks += 1
            return
        self.mark -= 1
        self.ticks = 0
        if self.mark < 0:
            return True
        if self.mark >= len(self.parts):
            return False
        part = self.parts.sprites()[self.mark]
        part.updateTick(self.x, self.y, self.collideWith, self.bullets, self.mark, self.direction, self.parts)
        return False