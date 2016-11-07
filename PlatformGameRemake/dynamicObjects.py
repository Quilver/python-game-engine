import physics

#I want all collision detection and all the objects to be managed by this class
class PhysicsEngine():
    def __init__(self, drag = 0.95, Gforce = 0.4):
        self.dynamic = []
        self.static = []
        self.player=None
        self.goal = None
        self.drag = drag
        self.Gforce = Gforce

#handle collisions
    def staticCollision(self):
        self.player.xVelocity, self.player.yVelocity = physics.collider(self.player.pos, self.static, self.player.xVelocity, self.player.yVelocity)
        if len(self.dynamic)>0:
            for i in self.dynamic:
                i.xVelocity, i.yVelocity = physics.collider(i.pos, self.static, i.xVelocity, i.yVelocity)
    def dynamicCollision(self):
        i = None
        counter = 0
        if len(self.dynamic)>0:
            for j in self.dynamic:
                physics.dynamicCollision(self.player, j)
                if counter!=0:
                    physics.dynamicCollision(i, j)
                i = j
                counter+=1


#lets the objects update themselves
    def update(self):
        if len(self.dynamic) > 0:
            for i in self.dynamic:
                i.update()
        self.player.update()
#enables viewpoint to change
    def camera(self):
        pass

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
        #adds in some decceleration and gravity
        self.decceleration()
        self.gravity()
        #all moving objects are updated
        self.update()
        #compares moving objects for collisions
        self.dynamicCollision()
        #compares moving to static objects for collisions
        self.staticCollision()

    def won(self):
        if physics.rectangleOverlap(self.player.pos, self.goal.pos):
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
    def __init__(self, x, y, width, length, engine, colour = "brown", density = 10,  dynamic = False, goal = False):
        #
        self.moment = 0
        self.xVelocity = 0
        self.yVelocity = 0
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



