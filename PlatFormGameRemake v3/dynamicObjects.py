import physics
import math

def Sort(array, index = None):
    if index != None:
        if len(array)-1>index:
            if array[index] > array[index+1]:
                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp
        if len(array) != 0 and index != 0:
            if array[index-1] < array[index]:
                temp = array[index]
                array[index] = array[index-1]
                array[index-1] = temp
    else:
        for j in range(len(array)):
            sorted = False
            for i in range(len(array)-1):
                if array[i] > array[i+1]:
                    sorted = True
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
            if not(sorted):
                break

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

#handle collisions
    def staticCollision(self):
        physics.boundingBoxTest(self.player, self.static)
        if len(self.dynamic)>0:
            for i in self.dynamic:
                physics.boundingBoxTest(i, self.static)
    def dynamicCollision(self):
        i = None
        counter = 0
        if len(self.dynamic)>0:
            for j in self.dynamic:
                physics.dynamicCollision(self.player, j)
                if counter!=0:
                    pass
                    #physics.dynamicCollision(i, j)
                i = j
                counter+=1


#lets the objects update themselves
    def update(self):
        if len(self.dynamic) > 0:
            for i in self.dynamic:
                i.update()
        self.player.update()
#enables viewpoint to change
    def camera(self, Xvelocity, Yvelocity):
        for i in self.static:
            i.move(Xvelocity, Yvelocity)
        for i in self.dynamic:
            i.move(Xvelocity, Yvelocity)

#adds gravity and acceleration
    def decceleration(self):
        self.player.xVelocity *= self.drag
        self.player.yVelocity *= self.drag
        if len(self.dynamic) > 0:
            for i in self.dynamic:
                i.xVelocity *= self.drag
                i.yVelocity *= self.drag
    def gravity(self):
        if len(self.dynamic)>0:
            for i in self.dynamic:
                i.yVelocity+=self.Gforce
        self.player.yVelocity+=self.Gforce

#updates the game each cycle
    def proccess(self):
        victory = self.won()
         #compares moving objects for collisions
        self.dynamicCollision()
        #compares moving to static objects for collisions
        self.staticCollision()
        #adds in some decceleration and gravity
        self.decceleration()
        self.gravity()
        #all moving objects are updated
        self.update()
        return victory

    def won(self):
        playerSpeed = physics.broadPhase(self.player.pos, [self.goal], self.player.xVelocity, self.player.yVelocity)
        if len(playerSpeed)>0:
            print("Victory")
            return False
        else:
            return True
    def reset(self):
        self.static = []
        self.dynamic = []
        self.player = None
        self.goal = None



#all 2d shapes are represented in abstract
class Rectangle():
    #equation of square |x-a|+|y-b| = c
    def __init__(self, x, y, width, length, engine, colour = "purple", density = 10,  dynamic = False, goal = False):
        #
        self.moment = 0
        self.xVelocity = 0
        self.yVelocity = 0
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
        self.dynamic = dynamic
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



