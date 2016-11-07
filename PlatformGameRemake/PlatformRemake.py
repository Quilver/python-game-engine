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
canvas.pack()

#
FPS = 1/12
engine = dynamicObjects.PhysicsEngine()

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
        if self.dynamic:
            self.move()
    def move(self):
        self.yVelocity-=0.3
        self.canvas.move(self.id, int(self.xVelocity), int(self.yVelocity))

class Player(dynamicObjects.Rectangle):
    def __init__(self, x, y, engine, colour = "brown", density = 100):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.yVelocity = 0
        self.width = 20
        self.length = 40
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
        self.jump_time_max = 190
        self.jump_time = self.jump_time_max
        #
        self.draw()
        engine.player = self
    def draw(self):
        self.id = [canvas.create_rectangle(self.x, self.y, self.x+20, self.y+40, fill="orange"), canvas.create_oval(self.x+5, self.y+9, self.x+7, self.y+11, fill="black"), canvas.create_oval(self.x+14, self.y+9, self.x+16, self.y+11, fill="black"), canvas.create_oval(self.x+5, self.y+18, self.x+15, self.y+25, fill="black")]
        self.stamina = canvas.create_rectangle(0,0,200, 25,fill="yellow")
        self.pos = self.canvas.coords(self.id[0])

    def update(self):
        self.pos = self.canvas.coords(self.id[0])
        self.motion()
        self.energy()
        self.move(self.xVelocity, self.yVelocity)

    def energy(self):
        if self.jump_time < self.jump_time_max:
            self.jump_time += 2
        self.canvas.delete(self.stamina)
        self.stamina=canvas.create_rectangle(0, 0, self.jump_time, 25, fill="purple")

    def move(self, xVelocity, yVelocity):
        self.canvas.move(self.id[0], int(xVelocity), int(yVelocity) )
        self.canvas.move(self.id[1], int(xVelocity), int(yVelocity) )
        self.canvas.move(self.id[2], int(xVelocity), int(yVelocity) )
        self.canvas.move(self.id[3], int(xVelocity), int(yVelocity) )
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
            self.yVelocity -= 0.9
            self.jump_time-=8
        if self.left:
            self.xVelocity -= 0.3
        elif self.right:
            self.xVelocity += 0.3

#sets up level
level = 7
while level <= 7:
    #sets up new level
    hasNotWon=True
    levelReader(level)

    #run game loop
    while hasNotWon:
        #runs all game logic per frame
        hasNotWon = engine.won()
        engine.proccess()
        #updates the graphics each frame
        tk.update_idletasks()
        tk.update()
        time.sleep(FPS)
    level+=1
    canvas.delete("all")
    engine.reset()
#shuts down window after game is finished
tk.destroy()