class Dynamic():
    def __init__(self, x, y, width, length, engine, canvas, colour= (0, 50, 200), density = 100):
        self.engine = engine
        self.canvas = canvas
        self.x = x
        self.y = y
        self.xAcceleration = 0
        self.YAcceleration = 0
        self.xVelocity = 0
        self.tempXv = self.xVelocity
        self.yVelocity = 0
        self.tempYv = self.yVelocity
        self.width = width
        self.length = length
        self.pos = [self.x, self.y, self.x+self.width, self.y+self.length]
        self.density = density
        self.colour = colour
        self.mass = self.density * self.width * self.length
        engine.dynamic.append(self)
        self.draw()
    def draw(self):
        pass
    def update(self):
        pass
    def move(self, xVelocity, yVelocity, timeFrame=1):
        self.pos[0] += int(xVelocity*timeFrame)
        self.pos[2] += int(xVelocity*timeFrame)
        self.pos[1] += int(yVelocity*timeFrame)
        self.pos[3] += int(yVelocity*timeFrame)
        if self.colour ==(100, 250, 100):
            self.canvas.move_image(self.id, int(xVelocity*timeFrame), int(yVelocity*timeFrame))
        else:
            self.canvas.move_rectangle(self.id, int(xVelocity*timeFrame), int(yVelocity*timeFrame))
        self.x+=int(xVelocity*timeFrame)
        self.y+=int(yVelocity*timeFrame)
        self.pos = [self.x, self.y, self.x+self.width, self.y+self.length]