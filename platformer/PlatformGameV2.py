from tkinter import *
import random
import time
import sys
#import QuinteMath
tk = Tk()
tk.title("Platform Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=900, height=700, bd=0, highlightthickness=0)
canvas.pack()


def collision(pos, momentum, y):
#stops the player from breaking moving through walls
    if pos[2]>=900 and momentum>0:
        if momentum>20:
            print(momentum)
            sys.exit()
        else:
            return momentum*-0.9, y
    elif pos[0]<=0 and momentum<0:
        if momentum<-20:
            print(momentum)
            sys.exit()
        else:
            return momentum*-0.9, y
    elif pos[3]>=700 and (y>0 or y<0):
        if y>0:
            return momentum, y*-0.4
        else:
            return momentum, y-1
        if (y>6 or y<-6):
            print(y)
            sys.exit()
    else:
        return momentum, y


class player():
    def __init__(self):
        self.canvas=canvas
        self.stamina=canvas.create_rectangle(0,0,30, 200,fill="yellow")
        self.id=[canvas.create_oval(0,0,20,20,fill="green"),canvas.create_oval(7,8,9,10,fill="black"),canvas.create_oval(12,8,14,10,fill="red")]
        self.canvas.move(self.id[0],300,300)
        self.canvas.move(self.id[1],300,300)
        self.canvas.move(self.id[2],300,300)
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

    def draw(self):
        self.physics()
    def physics(self):
        self.pos = self.canvas.coords(self.id[0])
        self.gravity()
        self.decceleration()
        self.motion()
        self.momentum, self.y=collision(self.pos, self.momentum, self.y)
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
        #if event.keysym=='space':
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

b=player()
while 1:
    b.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)
