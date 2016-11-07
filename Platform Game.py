from tkinter import *
import random
import time
tk = Tk()
tk.title("Platform Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=900, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
class thing:
    pass

class player(thing):
    def __init__(self,something):
        self.canvas=canvas
        self.id=[canvas.create_oval(0,0,20,20,fill="green"),canvas.create_oval(7,8,9,10,fill="black"),canvas.create_oval(12,8,14,10,fill="red")]
        self.something=something
        self.canvas.move(self.id[0],300,300)
        self.canvas.move(self.id[1],300,300)
        self.canvas.move(self.id[2],300,300)
#set it up for movement and flight
        self.canvas.bind_all('<space>',self.move)
        self.canvas.bind_all('<Left>', self.move)
        self.canvas.bind_all('<Right>', self.move)
        self.momentum=0
        self.fly=False
        self.jump_time=400
        self.y=0
        
    def draw(self):
        pos = self.canvas.coords(self.id[0])
        #enables the player to move up
        if self.fly and self.jump_time>=0:
            self.y-=0.45
            self.jump_time-=5
            self.fly=False
        if self.jump_time<400:
            self.jump_time+=1
       
#gravity affect and energy bar for flight
        self.y+=0.25
        stamina=canvas.create_rectangle(0,0,30,self.jump_time,fill="yellow")
        if self.death_x(pos) == True:
            self.momentum*= -0.95
        if self.death_y(pos) == True:
            self.y*=-1
#stops the player from breaking moving through walls
        if pos[2]>=900 and self.momentum>0:
            self.momentum*=-0.95
            
        if pos[0]<=0 and self.momentum<0:
            self.momentum*=-0.95
            
        if pos[3]>=700 and self.y>0:
            self.y*=-0.2
#enables decceleration 
        if self.momentum>0:
            self.momentum*=0.95
        if self.momentum<0:
            self.momentum*=0.95
            
#moves the player. Placed at the end of the of the function to stop it going through walls
        self.canvas.move(self.id[0],self.momentum,self.y)
        self.canvas.move(self.id[1],self.momentum,self.y)
        self.canvas.move(self.id[2],self.momentum,self.y)

    def move(self,event):
#when the keys are pressed will accelerate the player
        if event.keysym=='Left':
            self.momentum-=1
        if event.keysym=='Right':
            self.momentum+=1
        if event.keysym=='space':
            self.fly=True

    def death_x(self,pos):
        something_pos=self.canvas.coords(self.something.id)
        if pos[2] >= something_pos[0] and pos[0] <= something_pos[2] or pos[0] >= something_pos[2] and pos[2] <= something_pos[0]:
            if pos[3] >= something_pos[1] and pos[3] <= something_pos[3] or pos[1] >= something_pos[3] and pos[3] <= something_pos[3]:
                return True
        
        return False
    def death_y(self,pos):
        something_pos=self.canvas.coords(self.something.id)
        if pos[3] >= something_pos[1] and pos[3] <= something_pos[3] or pos[1] >= something_pos[3] and pos[3] <= something_pos[3]:
            if pos[2] >= something_pos[0] and pos[0] <= something_pos[2] or pos[0] >= something_pos[2] and pos[2] <= something_pos[0]:
                return True
        return False
    
class platform():
    def __init__(self,width,height,colour):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,width,height,fill=colour)
        self.canvas.move(self.id,700,600)
        
    def murder(self,player):
        pos = self.canvas.coords(self.id)
        player_location=self.canvas.coords(self.palyer.id[0])
        
meteor=platform(20,20,"grey")
b=player(meteor)
while 1:
    b.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)
