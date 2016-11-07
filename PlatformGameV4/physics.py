import sys
def quit():
    sys.exit()
def collision(pos, momentum, y):
#stops the player from breaking moving through walls
    if pos[2]>=1100 and momentum>0:
        if momentum>20:
            print(momentum)
            sys.exit()
        else:
            return momentum*-0.8, y
    elif pos[0]<=0 and momentum<0:
        if momentum<-20:
            print(momentum)
            sys.exit()
        else:
            return momentum*-0.8, y
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


#collision with blocks
def rectangleOverlap(dynamic, block, momentum, y):
    if (dynamic[2]>=block[0]) and (dynamic[0]<=block[2]):
            if (dynamic[3]>=block[1]) and (dynamic[1]<=block[3]):
                return True
    return False


#detects which plane the rectangles overlapped in
def quickCollide(dynamic, block, momentum, y):
     width = (dynamic[2]-dynamic[0])*0.5
     height = (dynamic[3]-dynamic[1])*0.5
     a=(dynamic[2]+dynamic[0])*.5
     b=(dynamic[1]+dynamic[3])*.5
     blockA = (block[2] + block[0]) * 0.5
     blockB = (block[3] + block[1]) * 0.5
     gradient = (block[3]-block[1]) / (block[2]-block[0])
     deltaX = abs( a - blockA )
     deltaY = abs( b - blockB)
     if deltaX!=0:
        deltaGradient = abs( deltaY / deltaX )
        if gradient > deltaGradient:
            momentum = hCollision(a, b, width, height, block, momentum)
        else:
            y = vCollision(a, b, width, height, block, y)

     else:
         y = vCollision(a, b, width, height, block, y)
     return momentum*0.6, y
# horizontal collision detection
def hCollision(a, b, width, height, block, momentum):
     if (a-width) <= block[0]:
        if momentum>0:
            momentum *= -1
        else:
            momentum=-1.1
        #
     elif (a+width) >= block[2]:
        if momentum<0:
            momentum *= -1
        else:
            momentum=1.1
     return momentum
#vertical collison detection
def vCollision(a, b, width, height, block, y):
    if (b-height) <= block[1]:
         if y>0:
            y *= -0.6
         else:
            y= -3
         #
    elif (b+height) >= block[3]:
        if y<0:
            y *= -0.6
        else:
            y = 3
    return y

def collider(dynamic, staticList, momentum, y):
    Collision=False
    for i in range(len(staticList)):
        block=staticList[i]
        if rectangleOverlap(dynamic, block, momentum, y):
            if (i+1) == len(staticList):
                return True, True
            else:
                momentum, y = quickCollide(dynamic, block, momentum, y)
    return momentum, y
