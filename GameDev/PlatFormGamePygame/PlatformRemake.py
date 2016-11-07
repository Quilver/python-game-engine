import time
import sys
import dynamicObjects
import Graphics
import pygame

#setting up engines
FPS = 1/60
engine = dynamicObjects.PhysicsEngine(FPS)
canvas = Graphics.GraphicsEngine()
def levelReader(level):
    fileName="level"+str(level)+".txt"
    MAP=open(fileName, 'r')
    for line in MAP:
        exec(str(line))
    MAP.close()

class Block(dynamicObjects.Rectangle):
    def draw(self):
        self.canvas = canvas
        self.mass = self.width * self.length

        if self.colour ==(100, 250, 100):
            self.id = canvas.create_image("brick.jpg", self.x, self.y, self.width, self.length)
        else:
            self.id = canvas.create_rectangle(self.colour, [self.x, self.y, self.width, self.length])
        self.pos = [self.x, self.y, self.x+self.width, self.x+self.length]
    def update(self):
        self.pos = [self.x, self.y, self.x+self.width, self.x+self.length]
    def move(self, xVelocity, yVelocity):
        if self.colour ==(100, 250, 100):
            self.canvas.move_image(self.id, int(xVelocity), int(yVelocity))
        else:
            self.canvas.move_rectangle(self.id, int(xVelocity), int(yVelocity))
        self.x+=int(xVelocity)
        self.y+=int(yVelocity)
        self.pos = [self.x, self.y, self.x+self.width, self.y+self.length]

class Player(dynamicObjects.Rectangle):
    def __init__(self, engine, density = 100):
        self.engine = engine
        self.x = 550
        self.y = 550
        self.xAcceleration = 20 * self.engine.FPS
        self.YAcceleration = 35 * self.engine.FPS
        self.xVelocity = 0
        self.yVelocity = 0
        self.width = 20
        self.length = 40
        self.density = density
        self.mass = self.density * self.width * self.length
        self.canvas = canvas
        #
        self.flight = False
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
    def draw(self):
         #self.id = [0, 0, 0, 0]
         #self.id[0] = canvas.create_rectangle((50, 150, 50), [self.x, self.y, self.width, self.length])
         #self.id[1] = canvas.create_rectangle((0,0,0), [self.x+5, self.y+9, 7, 7])
         #self.id[2] = canvas.create_rectangle((0,0,0), [self.x+14, self.y+9, 7, 7])
         #self.id[3] = canvas.create_rectangle((0,0,0), [self.x+5, self.y+18, 10, 5])
        self.id=canvas.create_image("character.png", 550, 550, self.width, self.length)
        self.stamina = canvas.create_rectangle((100, 100, 0), [0,0,200, 25])
        self.pos = [550, 550, 570, 590]
        self.move(-500, 0)
    def animation(self):
        if int(self.yVelocity)<0:
            canvas.replace_image(self.id, "jump2.png", 550, 550, self.width, self.length)
            if self.xVelocity<0:
                image = pygame.transform.flip(canvas.images[self.id][0], True, False)
                canvas.images[self.id][0] = image
        elif int(self.xVelocity)!=0:
            self.runAnimation()
        else:
            canvas.replace_image(self.id, "character.png", 550, 550, self.width, self.length)


    def runAnimation(self):
        if self.frame == 0:
            canvas.replace_image(self.id, "run1.png", 550, 550, self.width, self.length)
            self.LeftFace = True
            if self.frameCounter<240:
                self.frameCounter=0
                self.frame = 1
            self.frameCounter+=1
        elif self.frame == 1:
            canvas.replace_image(self.id, "run2.png", 550, 550, self.width, self.length)
            self.LeftFace = True
            if self.frameCounter<240:
                self.frameCounter=0
                self.frame = 2
            self.frameCounter+=1
        else:
            canvas.replace_image(self.id, "run3.png", 550, 550, self.width, self.length)
            self.LeftFace = True
            if self.frameCounter<240:
                self.frameCounter=0
                self.frame = 0
            self.frameCounter+=1
        if self.xVelocity>0:
            if self.leftFace:
                image = pygame.transform.flip(canvas.images[self.id][0], True, False)
                canvas.images[self.id][0] = image
                self.LeftFace = True
        else:
            if not(self.leftFace):
                image = pygame.transform.flip(canvas.images[self.id][0], True, False)
                canvas.images[self.id][0] = image
                self.LeftFace = False

    def update(self):
        self.centre = [ self.pos[0]+0.5*self.width, self.pos[1]+0.5*self.length]
        self.motion()
        self.energy()
        self.animation()
        #self.move(self.xVelocity, self.yVelocity)

    def energy(self):
        if self.jump_time < self.jump_time_max:
            self.jump_time += 100 * engine.FPS
        self.canvas.rectangles[self.stamina] = [(0, 0, 0), [0, 0, self.jump_time, 25]]

    def move(self, xVelocity, yVelocity):
        self.engine.camera(-xVelocity, -yVelocity)

        #self.canvas.move(self.id[0], int(xVelocity), int(yVelocity) )
        #self.canvas.move(self.id[1], int(xVelocity), int(yVelocity) )
        #self.canvas.move(self.id[2], int(xVelocity), int(yVelocity) )
        #self.canvas.move(self.id[3], int(xVelocity), int(yVelocity) )

        #self.pos = self.canvas.coords(self.id[0])
#when the keys are pressed will accelerate the player
    def fly(self):
        self.flight=True
    def moveL(self):
        self.left=True
    def moveR(self):
        self.right=True

    def stop(self, event):
        if event==pygame.K_LEFT:
            self.flight=False
        elif event==pygame.K_RIGHT:
            self.left=False
        elif event==pygame.K_UP:
            self.right=False
    def motion(self):
        if (self.jump_time>=0) and (self.flight):
            self.yVelocity -= self.YAcceleration
            self.jump_time-=400*engine.FPS
        if self.left:
            self.xVelocity -= self.xAcceleration
        elif self.right:
            self.xVelocity += self.xAcceleration

class Enemy(dynamicObjects.Rectangle):
    def draw(self):
        self.dynamic = True
        self.canvas = canvas
        self.mass = self.width * self.length
        self.id = canvas.create_rectangle((0, 250, 0),(self.x, self.y, self.x+self.width, self.y+self.length))
        self.pos = self.canvas.coords(self.id)
    def update(self):
        pass

#sets up level
level = 1
while level <= 6:
    #sets up new level
    hasNotWon=True
    levelReader(level)
    #run game loop
    while hasNotWon:
        deltaFps =time.time()
        canvas.draw()
         #runs all game logic per frame
        hasNotWon = engine.proccess()
         #updates the graphics each frame
        Graphics.playerInput(engine.player)
        deltaFps-= time.time()
        deltaFps *= -1
        #print(deltaFps)
        if deltaFps<FPS:
            time.sleep(FPS-deltaFps)
        #if deltaFps!=0:
        #    print(int(1/deltaFps))
    level+=1
    canvas.reset()
    engine.reset()
#shuts down window after game is finished
Graphics.terminate()