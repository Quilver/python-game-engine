class Rectangle():
    def __init__(self, x, y, width, length, engine, canvas, colour = (100, 250, 100), density = 10):
        #
        self.moment = 0
        self.xVelocity = 0
        self.tempXv = self.xVelocity
        self.yVelocity = 0
        self.tempYv = self.yVelocity
        self.canvas = canvas
        #
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.centre = [ self.x+0.5*self.width, self.y+0.5*self.length]
        #
        self.colour = colour
        self.density = density
        self.mass = self.density * width * length
        self.engine = engine
        self.engine.static.append(self)
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
    #this part will be complicated to implement
    def rotation(self):
        #moment equations to remember are moment = F*d
        #d is distance from center of mass
        #moment will be the anticlockwise rotation
        pass