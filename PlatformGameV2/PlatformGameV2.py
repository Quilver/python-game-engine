from tkinter import *
import random
import time
#import staticObjects
#from dynamicObjects
import sys
import physics
#import QuinteMath
tk = Tk()
tk.title("Platform Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=900, height=700, bd=0, highlightthickness=0)
canvas.pack()

WALL=[]


class Block():
    def __init__(self, x, y):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.id=canvas.create_rectangle(self.x, self.y, self.x+20, self.y+20,fill="brown")
        self.pos=self.canvas.coords(self.id)
        WALL.append(self.pos)

class Player():
    def __init__(self):
        self.canvas=canvas
        self.stamina=canvas.create_rectangle(0,0,30, 200,fill="yellow")
        self.id=[canvas.create_oval(0,0,20,20,fill="green"),canvas.create_oval(7,8,9,10,fill="black"),canvas.create_oval(12,8,14,10,fill="red")]
        self.canvas.move(self.id[0],300,300)
        self.canvas.move(self.id[1],300,300)
        self.canvas.move(self.id[2],300,300)
        self.pos = self.canvas.coords(self.id[0])
#set it up for movement and flight
        self.canvas.bind_all('<space>',self.fly)
        self.canvas.bind_all('<KeyRelease>',self.stop)
        self.canvas.bind_all('<Left>', self.moveL)
        self.canvas.bind_all('<Right>', self.moveR)
        self.momentum=0
        self.flight=False
        self.left=False
        self.right=False
        self.jump_time=150
        self.y=0

    def draw(self, static):
        self.static=static
        self.physics()
    def physics(self):
        self.pos = self.canvas.coords(self.id[0])
        self.gravity()
        self.decceleration()
        self.motion()
        #collision
        self.momentum, self.y=physics.collider(self.pos, self.static, self.momentum, self.y)
        self.momentum, self.y=physics.collision(self.pos, self.momentum, self.y)
        #moves the player. Placed at the end of the of the function to stop it going through walls

        self.canvas.move(self.id[0],self.momentum,self.y)
        self.canvas.move(self.id[1],self.momentum,self.y)
        self.canvas.move(self.id[2],self.momentum,self.y)


    def gravity(self):

#gravity affect and energy bar for flight
        if self.jump_time<=150:
            self.jump_time+=2
        self.y+=1.1
        self.canvas.delete(self.stamina)
        self.stamina=canvas.create_rectangle(0,0,30,self.jump_time,fill="yellow")


    def decceleration(self):
#enables decceleration
        if self.momentum!=0:
            self.momentum*=0.91
        if self.y!=0:
            self.y*=0.96

    def stop(self, event):
        if event.keysym=='space':
            self.flight=False
        elif event.keysym=='Left':
            self.left=False
        elif event.keysym=='Right':
            self.right=False

    def fly(self,event):
#when the keys are pressed will accelerate the player
        self.flight=True

    def motion(self):
        if (self.jump_time>=0) and (self.flight):
            self.y-=2
            self.jump_time-=10
        if self.left:
            self.momentum-=1.7
        elif self.right:
            self.momentum+=1.7
    def moveL(self,event):
        self.left=True
        #if event.keysym=='Left':

    def moveR(self,event):
        #elif event.keysym=='Right':
        self.right=True
block1=Block(350, 620)
block2=Block(400, 660)
block3=Block(350, 640)
block3=Block(350, 680)
character=Player()
#print(character.pos)
#print(WALL)
while 1:
    character.draw(WALL)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)
