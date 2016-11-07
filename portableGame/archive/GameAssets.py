import dynamicObjects as dynamicObjects
from assets.parents import Graphics as Graphics
import pygame
def stop(objectM, phase):
    if phase == "x":
        objectM.xVelocity = 0
        objectM.tempXv = 0
    else:
        objectM.yVelocity = 0
        objectM.tempYv = 0
def bounce(objectM, phase):
    if phase == "x":
        objectM.xVelocity *= -1
        objectM.tempXv *= -1
    else:
        objectM.yVelocity = 0
        objectM.tempYv = 0
def shove(object1, object2, phase):
    if phase == "x":
        if abs(object1.xVelocity)>abs(object2.xVelocity):
            if object1.xVelocity != object2.xVelocity:
                object2.xVelocity = object1.xVelocity
                object2.tempXv = object1.tempXv
    else:
        if abs(object1.yVelocity)>abs(object2.yVelocity):
            if object1.yVelocity != object2.yVelocity:
                object2.yVelocity = object1.yVelocity
                object2.tempYv = object1.tempYv

def losslessCollision(object1, object2, phase):
    #E=(mV^2)/2, p = m*v
    if phase == "x":
        object1.xVelocity = (object1.xVelocity*object1.mass + object2.xVelocity*object2.mass)/(object1.mass+object2.mass)
        object2.xVelocity = object1.xVelocity
        object1.tempXv = (object1.tempXv*object1.mass + object2.tempXv*object2.mass)/(object1.mass+object2.mass)
        object2.tempXv = object1.tempXv
    else:
        object1.yVelocity = (object1.yVelocity*object1.mass + object2.yVelocity*object2.mass)/(object1.mass+object2.mass)
        object2.yVelocity = object1.yVelocity
        object1.tempYv = (object1.tempYv*object1.mass + object2.tempYv*object2.mass)/(object1.mass+object2.mass)
        object2.tempYv = object1.tempYv
class Background():
    def __init__(self, engine, canvas):
        self.x, self.y = -500, -500
        self.width, self.length = 2000, 2000
        self.canvas = canvas
        self.id = self.canvas.create_image("background.png", self.x, self.y, self.width, self.length)
        engine.background.append(self)
    def move(self, xVelocity, yVelocity, timeFrame =1):
        self.canvas.move_image(self.id, int(xVelocity*timeFrame/2), int(yVelocity*timeFrame/2))
class Candle():
    def __init__(self, engine, canvas, x, y):
        self.x, self.y = x, y
        self.width, self.length = 20, 20
        self.canvas = canvas
        self.id = self.canvas.create_image("candle.png", self.x, self.y, self.width, self.length)
        engine.background.append(self)
    def move(self, xVelocity, yVelocity, timeFrame =1):
        self.canvas.move_image(self.id, int(xVelocity*timeFrame), int(yVelocity*timeFrame))
class Block(dynamicObjects.Rectangle):
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
class Wall(dynamicObjects.Rectangle):
    def draw(self):
        self.name = "wall"
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
        stop(objectM, phase)

class Goal(dynamicObjects.Rectangle):
    def draw(self):
        self.name = "goal"
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
        if objectM.name == "player":
            self.engine.victory = False
        if phase == "x":
            objectM.xVelocity = 0
            objectM.tempXv = 0
        else:
            objectM.yVelocity = 0
            objectM.tempYv = 0

class Player(dynamicObjects.Rectangle):
    def __init__(self, engine, canvas, density = 0.001):
        self.name = "player"
        self.engine = engine
        self.x = 550
        self.y = 550
        self.xAcceleration = 20 * self.engine.FPS
        self.YAcceleration = 20 * self.engine.FPS
        self.xVelocity = 0
        self.maxX = 15
        self.tempXv = self.xVelocity
        self.yVelocity = 0
        self.maxY = 10
        self.tempYv = self.yVelocity
        self.slowing = self.xAcceleration/3
        self.width = 40
        self.length = 40
        self.density = density
        self.mass = self.density * self.width * self.length
        self.canvas = canvas
        #
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        #
        self.jump_time_max = 300
        self.jump_time = self.jump_time_max
        self.frameCounter = 0
        self.frame = True
        self.leftFace = False
        #
        self.draw()
        engine.player = self
        engine.dynamic.append(self)
    def draw(self):
        self.id=self.canvas.create_image("character.png", 550, 550, self.width, self.length)
        self.stamina = self.canvas.create_rectangle((100, 100, 0), [0,0,200, 25])
        self.pos = [self.x, self.y, self.x+self.width, self.y+self.width]
        self.move(-500, 0)
    def animation(self):
        if int(self.yVelocity)<0:
            self.canvas.replace_image(self.id, "jump2.png", 550, 550, self.width, self.length)
            if self.xVelocity<0:
                image = pygame.transform.flip(self.canvas.images[self.id][0], True, False)
                self.canvas.images[self.id][0] = image
        elif int(self.xVelocity)!=0:
            self.runAnimation()
        else:
            self.canvas.replace_image(self.id, "character.png", 550, 550, self.width, self.length)


    def runAnimation(self):
        if self.frame == 0:
            self.canvas.replace_image(self.id, "run1.png", 550, 550, self.width, self.length)
            self.LeftFace = True
            if self.frameCounter>5:
                self.frameCounter=0
                self.frame = 1
            self.frameCounter+=1
        elif self.frame == 1:
            self.canvas.replace_image(self.id, "run2.png", 550, 550, self.width, self.length)
            self.LeftFace = True
            if self.frameCounter>5:
                self.frameCounter=0
                self.frame = 2
            self.frameCounter+=1
        else:
            self.canvas.replace_image(self.id, "run3.png", 550, 550, self.width, self.length)
            self.LeftFace = True
            if self.frameCounter<5:
                self.frameCounter=0
                self.frame = 0
            self.frameCounter+=1
        if self.xVelocity>0:
            if self.leftFace:
                image = pygame.transform.flip(self.canvas.images[self.id][0], True, False)
                self.canvas.images[self.id][0] = image
                self.LeftFace = True
        else:
            if not(self.leftFace):
                image = pygame.transform.flip(self.canvas.images[self.id][0], True, False)
                self.canvas.images[self.id][0] = image
                self.LeftFace = False

    def update(self):
        self.motion()
        self.energy()
        self.animation()
        Graphics.TopDownPlayer(self)
        #self.move(self.xVelocity, self.yVelocity)

    def energy(self):
        if self.jump_time < self.jump_time_max:
            self.jump_time += 100 * self.engine.FPS
        self.canvas.rectangles[self.stamina] = [(0, 0, 0), [0, 0, self.jump_time, 25]]

    def move(self, xVelocity, yVelocity, timeFrame = 1):
        self.engine.camera(-int(xVelocity*timeFrame), -int(yVelocity*timeFrame))

#when the keys are pressed will accelerate the player
    def motion(self):
        if (self.up) and (self.yVelocity>(-self.maxY)):
            self.yVelocity -= self.YAcceleration
        elif (self.down) and (self.yVelocity< self.maxY):
            self.yVelocity += self.YAcceleration
        else:
            if abs(self.yVelocity)-self.slowing == 0:
                self.yVelocity = 0
            elif self.yVelocity>0:
                self.yVelocity -= self.slowing
            else:
                self.yVelocity += self.slowing
        if self.left and (self.xVelocity>(-self.maxX)):
            self.xVelocity -= self.xAcceleration
        elif self.right and (self.xVelocity<(self.maxX)):
            self.xVelocity += self.xAcceleration
        else:
            if abs(self.xVelocity)-self.slowing <= 0:
                self.xVelocity = 0
            elif self.xVelocity>0:
                self.xVelocity -= self.slowing
            else:
                self.xVelocity += self.slowing
    def act(self, objectM, phase):
        if objectM.name == "player" or "dynamic" == objectM.name:
            pass
            #losslessCollision(self, objectM, phase)
class Enemy(dynamicObjects.Dynamic):
    def draw(self):
        self.mass = 3.2
        self.xVelocity = -20 * self.engine.FPS
        self.name = "dynamic"
        if self.colour ==(100, 250, 100):
            self.id = self.canvas.create_image("brick.jpg", self.x, self.y, self.width, self.length)
        else:
            self.id = self.canvas.create_rectangle(self.colour, [self.x, self.y, self.width, self.length])
        self.pos = [self.x, self.y, self.x+self.width, self.x+self.length]
    def update(self):
        self.xVelocity += 0.06
        self.yVelocity /= 1.1
    def act(self, objectM, phase):
        if objectM.name == "player" or "dynamic" == objectM.name:
            losslessCollision(self, objectM, phase)
