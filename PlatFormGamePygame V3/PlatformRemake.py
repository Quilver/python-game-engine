from tkinter import *
import random
import time
import sys
import dynamicObjects
tk = Tk()
tk.title("Platform Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1100, height=700, bd=0, highlightthickness=0)
canvas.pack(expand = YES, fill = BOTH)
#
FPS = 1/60
engine = dynamicObjects.PhysicsEngine(FPS)

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
        self.id = canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.length,fill=self.colour)
        self.pos = self.canvas.coords(self.id)
    def update(self):
        self.pos = self.canvas.coords(self.id)
        self.centre = [ self.pos[0]+0.5*self.width, self.pos[1]+0.5*self.length]
        #if self.dynamic:
        #    self.move(self.xVelocity, self.yVelocity)
    def move(self, xVelocity, yVelocity):
        self.canvas.move(self.id, int(xVelocity), int(yVelocity))
        self.pos = self.canvas.coords(self.id)

class Player(dynamicObjects.Rectangle):
    def __init__(self, engine, colour = "brown", density = 100):
        self.engine = engine
        self.x = 550
        self.y = 550
        self.xAcceleration = 20 * self.engine.FPS
        self.YAcceleration = 35 * self.engine.FPS
        self.xVelocity = 0
        self.yVelocity = 0
        self.width = 20
        self.length = 40
        self.centre = [ self.x+0.5*self.width, self.y+0.5*self.length]
        self.colour = colour
        self.density = density
        self.mass = self.density * self.width * self.length
        self.canvas = canvas
        #set it up for movement and flight
        self.canvas.bind_all('<space>',self.fly)
        self.canvas.bind_all('<KeyRelease>',self.stop)
        self.canvas.bind_all('<Left>', self.moveL)
        self.canvas.bind_all('<Right>', self.moveR)
        #
        self.flight = False
        self.left = False
        self.right = False
        #
        self.jump_time_max = 300
        self.jump_time = self.jump_time_max
        #
        self.draw()
        engine.player = self
    def draw(self):
        #self.id = [canvas.create_rectangle(self.x, self.y, self.x+20, self.y+40, fill="orange"), canvas.create_oval(self.x+5, self.y+9, self.x+7, self.y+11, fill="black"), canvas.create_oval(self.x+14, self.y+9, self.x+16, self.y+11, fill="black"), canvas.create_oval(self.x+5, self.y+18, self.x+15, self.y+25, fill="black")]
        self.stamina = canvas.create_rectangle(0,0,200, 25,fill="yellow")
        #canvas.create_image(0, 0, image = gif1, anchor = NW)
        #self.pos = self.canvas.coords(self.id[0])
        self.pos = [550, 550, 570, 590]
        self.move(-500, 0)
    def update(self):
        self.centre = [ self.pos[0]+0.5*self.width, self.pos[1]+0.5*self.length]
        self.motion()
        self.energy()
        #self.move(self.xVelocity, self.yVelocity)

    def energy(self):
        if self.jump_time < self.jump_time_max:
            self.jump_time += 100 * engine.FPS
        self.canvas.delete(self.stamina)
        self.stamina=canvas.create_rectangle(0, 0, self.jump_time, 25, fill="yellow")

    def move(self, xVelocity, yVelocity):
        self.engine.camera(-xVelocity, -yVelocity)

        #self.canvas.move(self.id[0], int(xVelocity), int(yVelocity) )
        #self.canvas.move(self.id[1], int(xVelocity), int(yVelocity) )
        #self.canvas.move(self.id[2], int(xVelocity), int(yVelocity) )
        #self.canvas.move(self.id[3], int(xVelocity), int(yVelocity) )

        #self.pos = self.canvas.coords(self.id[0])
#when the keys are pressed will accelerate the player
    def fly(self,event):
        self.flight=True
    def moveL(self,event):
        self.left=True
    def moveR(self,event):
        self.right=True

    def stop(self, event):
        if event.keysym=='space':
            self.flight=False
        elif event.keysym=='Left':
            self.left=False
        elif event.keysym=='Right':
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
        self.colour = "red"
        self.dynamic = True
        self.canvas = canvas
        self.mass = self.width * self.length
        self.id = canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.length,fill=self.colour)
        self.pos = self.canvas.coords(self.id)
    def update(self):
        pass

#sets up level
level = 1
while level <= 6:
    #sets up new level
    hasNotWon=True
    canvas.create_image(0, 0, image = gif1, anchor = NW)
    levelReader(level)
    playerImage = PhotoImage(file = 'character.gif')
    engine.player.pos = canvas.coords(playerImage)
    #run game loop
    while hasNotWon:
        deltaFps =time.time()
        #runs all game logic per frame
        hasNotWon = engine.proccess()
        #updates the graphics each frame
        tk.update_idletasks()
        tk.update()
        deltaFps-= time.time()
        deltaFps *= -1
        print(deltaFps)
        if deltaFps<FPS:
            time.sleep(FPS-deltaFps)
        print(int(1/deltaFps))
    level+=1
    canvas.delete("all")
    engine.reset()
#shuts down window after game is finished
tk.destroy()