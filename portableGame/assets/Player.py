from assets.parents.Hit import*
from assets.parents import Graphics as Graphics
import pygame
def Activate():
    print("hello")
class Player():#Rectangle):
    def __init__(self, engine, canvas, density = 100):
        #importing modules
        #setting up variables
        self.name = "player"
        self.engine = engine
        self.x = 550
        self.y = 550
        self.xAcceleration = 20 * self.engine.FPS
        self.YAcceleration = 35 * self.engine.FPS
        self.xVelocity = 0
        self.maxX = 10
        self.tempXv = self.xVelocity
        self.yVelocity = 0
        self.maxY = 5
        self.tempYv = self.yVelocity
        self.slowing = 10 * self.engine.FPS
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
            shove(self, objectM, phase)