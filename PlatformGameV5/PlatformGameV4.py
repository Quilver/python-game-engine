from tkinter import *
import random
import time
import sys
import physics
tk = Tk()
tk.title("Platform Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1100, height=700, bd=0, highlightthickness=0)
canvas.pack()
#canvas.bind_all('<Esc>', physics.quit)


class Block():
    def __init__(self, x, y, width=50, length=5, colour="brown", moving=False):
        self.canvas=canvas
        self.x = x
        self.y = y
        self.id = canvas.create_rectangle(self.x, self.y, self.x+width, self.y+length,fill=colour)
        self.pos = self.canvas.coords(self.id)
        if moving:
            self.velocity=10
            #add to a dynamic list

        self.i=len(WALL)
        WALL.append(self.pos)
    def chase(self, posOfObject):
        self.pos = self.canvas.coords(self.id)
        WALL[self.i]=self.pos
        deltaX = posOfObject[0]-(self.pos[0]+self.pos[2])*0.5
        deltaY = posOfObject[1]-(self.pos[1]+self.pos[3])*0.5
        deltaTotal = abs(deltaX) + abs(deltaY)
        if deltaTotal!=0:
            self.xSpeed = int(self.velocity * (deltaX/deltaTotal) )
            self.ySpeed = int(self.velocity * (deltaY/deltaTotal) )
            self.canvas.move(self.id, self.xSpeed, self.ySpeed)


class Player():
    def __init__(self, x=300, y=660, mass=10):
        self.canvas = canvas
        self.stamina = canvas.create_rectangle(0,0,200, 25,fill="yellow")
        self.id = [canvas.create_rectangle(x, y, x+20, y+40, fill="orange"), canvas.create_oval(x+5, y+9, x+7, y+11, fill="black"), canvas.create_oval(x+14, y+9, x+16, y+11, fill="black"), canvas.create_oval(x+5, y+18, x+15, y+25, fill="black")]
        self.pos = self.canvas.coords(self.id[0])
        self.mass = mass
#set it up for movement and flight
        self.canvas.bind_all('<space>',self.fly)
        self.canvas.bind_all('<KeyRelease>',self.stop)
        self.canvas.bind_all('<Left>', self.moveL)
        self.canvas.bind_all('<Right>', self.moveR)
        self.momentum = 0
        self.flight = False
        self.left = False
        self.right = False
        self.jump_time = 150
        self.y = 0

    def draw(self, static):
        self.static=static
        return self.physics()
    def physics(self):
        self.pos = self.canvas.coords(self.id[0])
        self.gravity()
        self.motion()
        #collision
        self.momentum, self.y = physics.collider(self.pos, self.static, self.momentum, self.y)
        if (self.momentum==True) and (self.y==True):
            return False
        #calculates player velocity
        self.decceleration()
        self.motion()
        #Placed at the end of the of the function to stop it going through walls
        self.momentum, self.y=physics.collision(self.pos, self.momentum, self.y)
        #moves the player.
        #print(self.momentum)
        self.canvas.move(self.id[0], int(self.momentum), int(self.y) )
        self.canvas.move(self.id[1], int(self.momentum), int(self.y) )
        self.canvas.move(self.id[2], int(self.momentum), int(self.y) )
        self.canvas.move(self.id[3], int(self.momentum), int(self.y) )

        return True
    def gravity(self):

#gravity affect and energy bar for flight
        if self.jump_time < 150:
            self.jump_time += 3
        self.y+=1
        self.canvas.delete(self.stamina)
        self.stamina=canvas.create_rectangle(0, 0, self.jump_time, 25, fill="purple")


    def decceleration(self):
#enables decceleration
        if self.momentum!=0:
            self.momentum*=0.94
        if self.y!=0:
            self.y*=0.96

    def stop(self, event):
        if event.keysym=='space':
            self.flight=False
        elif event.keysym=='Left':
            self.left=False
        elif event.keysym=='Right':
            self.right=False
#when the keys are pressed will accelerate the player
    def fly(self,event):

        self.flight=True

    def motion(self):
        if (self.jump_time>=0) and (self.flight):
            self.y-=1.5
            self.jump_time-=10
        if self.left:
            self.momentum -= 0.4
        elif self.right:
            self.momentum += 0.4
    def moveL(self,event):
        self.left=True

    def moveR(self,event):
        self.right=True

#sets up level
level=1
while level <= 6:
    hasNotWon=True
    fileName="level"+str(level)+".txt"
    WALL = []
    MOVING_OBJECTS = []
    MAP=open(fileName, 'r')
    for line in MAP:
        exec(str(line))
    MAP.close()
    while hasNotWon:
        if level==7:
            chaser.chase(character.pos)
        hasNotWon=character.draw(WALL)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.02)
    canvas.delete("all")
    del character
    level+=1
#shuts down window after game is finished
tk.destroy()
