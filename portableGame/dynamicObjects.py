import physics as physics
import math, time


#I want all collision detection and all the objects to be managed by this class
class PhysicsEngine():
    def __init__(self, FPS = 1/60, drag = 0.9, Gforce = 24):
        self.FPS = FPS
        self.dynamic = []
        self.static = []
        self.background = []
        self.goal = None
        if (drag > 0) and (drag < 1):
            self.drag = 1 - math.log(drag, FPS)
        else:
            self.drag = 1
        self.Gforce = Gforce * FPS
        self.victory = True
#handle collisions
    def collision(self):
        physics.start(self.dynamic, self.static)
#lets the objects update themselves
    def update(self):
        for i in self.dynamic:
            i.update()
#enables viewpoint to change
    def camera(self, Xvelocity, Yvelocity):
        for i in self.background:
            i.move(Xvelocity, Yvelocity)
        for i in self.dynamic:
            if i.name != "player":
                i.move(Xvelocity, Yvelocity)
        for i in self.static:
            i.move(Xvelocity, Yvelocity)

#adds gravity and acceleration
    def decceleration(self):
        if len(self.dynamic) > 0:
            for i in self.dynamic:
                i.xVelocity *= self.drag
                i.yVelocity *= self.drag
    def gravity(self):
        if len(self.dynamic)>0:
            for i in self.dynamic:
                i.yVelocity+=self.Gforce

#updates the game each cycle
    def proccess(self):
         #compares objects for collisions
        self.collision()
         #adds in some decceleration and gravity
        self.decceleration()
        self.gravity()
         #all moving objects are updated
        self.update()
        return self.victory

    def reset(self):
        self.static = []
        self.dynamic = []
        self.background =[]
        self.player.canvas.reset()
        self.player = None
        self.goal = None
        self.victory = True



#all 2d shapes are represented in abstract
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

class Circle():
    def __init__(self, x, y, radius, engine,  colour = "red", density = 10, dynamic = False):
        if dynamic:
            engine.dynamic.append(self)
        else:
            engine.static.append(self)
    def draw(self):
        pass
    def update(self):
        pass
    def move(self):
        pass