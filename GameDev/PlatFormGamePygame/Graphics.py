import random
import sys
import pygame
import copy
import time
from pygame.locals import*
pygame.init()
def terminate():
    pygame.quit()
    sys.exit()

class GraphicsEngine():
    def __init__(self):
        self.canvas = pygame.display.set_mode((1100,700))
        self.background= None
        self.images =[]
        self.rectangles = []
        self.black=pygame.Color(0,0,0)
        self.red=pygame.Color(95, 15, 15)
        self.grey=pygame.Color(40,40,40)
        self.white=pygame.Color(250,250,250)
        self.green=pygame.Color(100,150,50)
    def create_image(self, fileName, x, y, width, height):
        id = len(self.images)
        image = pygame.image.load(fileName)
        image=pygame.transform.smoothscale(image, (int(width), int(height)))
        self.images.append([image, [x, y]])
        return id
    def replace_image(self, id, fileName, x, y, width, height):
        image = pygame.image.load(fileName)
        image=pygame.transform.smoothscale(image, (int(width), int(height)))
        self.images[id] = [image, [x, y]]
    def move_image(self, id, Xvelocity, Yvelocity):
        self.images[id][1][0]+= Xvelocity
        self.images[id][1][1]+= Yvelocity
    def draw_image(self, id):
        self.canvas.blit(id[0], id[1])
    def create_rectangle(self, colour, pos):
        id = len(self.rectangles)
        rect = [colour, [pos]]
        self.rectangles.append([rect[0], rect[1]])
        return id
    def draw_rectangle(self, rectangle):
        try:
            pygame.draw.rect(self.canvas, rectangle[0], rectangle[1][0])
        except:
            #print(rectangle)
            pygame.draw.rect(self.canvas, rectangle[0], rectangle[1])
    def move_rectangle(self, id, Xvelocity, Yvelocity):
        rectangle = self.rectangles[id]
        pos = rectangle[1]
        pos[0][0] += Xvelocity
        pos[0][1] += Yvelocity
        rectangle[1] = pos
        self.rectangles[id] = rectangle
    def coords(self, id):
        if len(self.rectangles)>1:
            rect = copy.deepcopy(self.rectangles[id][1][0])
            return rect[0], rect[1], rect[0]+rect[2], rect[1]+rect[3]
        else: return self.rectangles
    def draw(self):
        self.canvas.fill((250,250,250))
        if len(self.rectangles)>0:
            for i in self.rectangles:
                self.draw_rectangle(i)

        if len(self.images)>0:
            for i in self.images:
                self.draw_image(i)
        pygame.display.update()
        #pygame.display.flip()
    def reset(self):
        self.rectangles = []
        self.images = []

def playerInput(self):
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            terminate()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.moveL()
            elif event.key == pygame.K_RIGHT:
                self.moveR()
            if event.key == pygame.K_UP:
                self.fly()
        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_UP:
                self.flight=False
