import Test as physics
import math
import time

#I want all collision detection and all the objects to be managed by this class
class PhysicsEngine():
    def __init__(self, FPS = 60, drag = 0.9, Gforce = 24):
        self.FPS = FPS
        self.dynamic = []
        self.static = []
        self.player=None
        self.goal = None
        self.drag = 1 - math.log(drag, FPS)
        self.Gforce = Gforce * FPS
        self.victory = True
#handle collisions
    def collision(self):
        #st = time.time()
        physics.start(self.dynamic, self.static)
        #st -= time.time()
        #print(1/(-st))
#lets the objects update themselves
    def update(self):
        for i in self.dynamic:
            i.update()
#enables viewpoint to change
    def camera(self, Xvelocity, Yvelocity):
        for i in self.static:
            i.move(Xvelocity, Yvelocity)
        for i in self.dynamic:
            if i != self.player:
                i.move(Xvelocity, Yvelocity)

#adds gravity and acceleration
    def decceleration(self):
        for i in self.dynamic:
            i.xVelocity *= self.drag
            i.yVelocity *= self.drag
    def gravity(self):
        for i in self.dynamic:
            i.yVelocity+=self.Gforce
        #self.player.yVelocity+=self.Gforce

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
        self.player = None
        self.goal = None
        self.victory =True



#all 2d shapes are represented in abstract
class Rectangle():
    #equation of square |x-a|+|y-b| = c
    def __init__(self, x, y, width, length, engine, colour = "purple", density = 10,  dynamic = False, goal = False):
        #
        self.moment = 0
        self.xVelocity = 0
        self.tempXv = self.xVelocity
        self.yVelocity = 0
        self.tempYv = self.yVelocity
        #
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        #
        self.colour = colour
        self.density = density
        self.mass = self.density * width * length
        self.dynamic = dynamic
        self.engine = engine
        if dynamic:
            engine.dynamic.append(self)
        else:
            engine.static.append(self)
        if goal:
            engine.goal = self
        self.draw()
    def draw(self):
        pass
    def update(self):
        pass
    def move(self):
        pass
    def act(self):
        pass
    #this part will be complicated to implement
    def rotation(self):
        #moment equations to remember are moment = F*d
        #d is distance from center of mass
        #moment will be the anticlockwise rotation
        pass

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



