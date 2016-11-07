#from parents import Rectangle
from assets.parents.Rectangle import Rectangle as Rectangle
from assets.parents.Hit import*
class Block(Rectangle):
    def draw(self):
        self.name = "bounceBlock"
        if self.colour ==(100, 250, 100):
            self.id = self.canvas.create_image("brick.jpg", self.x, self.y, self.width, self.length)
        else:
            self.id = self.canvas.create_rectangle(self.colour, [self.x, self.y, self.width, self.length])
        self.pos = [self.x, self.y, self.x+self.width, self.x+self.length]
    def move(self, xVelocity, yVelocity):
        self.pos[0] += int(xVelocity)
        self.pos[2] += int(xVelocity)
        self.pos[1] += int(yVelocity)
        self.pos[3] += int(yVelocity)
        if self.colour ==(100, 250, 100):
            self.canvas.move_image(self.id, int(xVelocity), int(yVelocity))
        else:
            self.canvas.move_rectangle(self.id, int(xVelocity), int(yVelocity))
        self.x+=int(xVelocity)
        self.y+=int(yVelocity)
        self.pos = [self.x, self.y, self.x+self.width, self.y+self.length]
    def act(self, objectM, phase):
        bounce(objectM, phase)