import sys
def quit():
    sys.exit()

#collision detection


#collision with blocks
def rectangleOverlap(dynamic, block):
    if (dynamic[2]>=block[0]) and (dynamic[0]<=block[2]):
            if (dynamic[3]>=block[1]) and (dynamic[1]<=block[3]):
                return True
    return False

#detects which plane the rectangles overlapped in
def lineCollide(dynamic, block):
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
            return "x"
        else:
            return "y"

     else:
         return "y"


#collision for static objects

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
        if gradient*1.01 >= deltaGradient:
            momentum = hCollision(a, b, width, height, block, momentum)
        if gradient*0.99 <= deltaGradient:
            y = vCollision(a, b, width, height, block, y)

     else:
         y = vCollision(a, b, width, height, block, y)
     return momentum, y
# horizontal collision detection
def hCollision(a, b, width, height, block, momentum):
     if (a-width) <= block[0]:
        if momentum>0:
            momentum *= -0.8
        else:
            momentum=-1
        #
     elif (a+width) >= block[2]:
        if momentum<0:
            momentum *= -0.8
        else:
            momentum=1
     return momentum
#vertical collison detection
def vCollision(a, b, width, height, block, y):
    if (b-height) <= block[1]:
         if y>0:
            y *= -0.8
         elif (y>-2) :
            y= -2
         #
    elif (b+height) >= block[3]:
        if y<0:
            y *= -0.8
        elif (y<2) :
            y = 2
    return y

def collider(dynamic, staticList, momentum, y):
    Collision=False
    for i in range(len(staticList)):
        block=staticList[i].pos
        if rectangleOverlap(dynamic, block):
            momentum, y = quickCollide(dynamic, block, momentum, y)
    return momentum, y


# Collision for dynamic objects
def xDynamic(object1, object2):
    v1 = (object1.xVelocity+ (object1.mass- object2.mass)+ 2*object2.mass*object2.xVelocity) / (object1.mass + object2.mass)
    v2 = (object2.xVelocity+ (object2.mass- object1.mass)+ 2*object1.mass*object1.xVelocity) / (object1.mass + object2.mass)
    #
    object1.xVelocity = v1
    object2.xVelocity = v2
def yDynamic(object1, object2):
    v1 = (object1.yVelocity+ (object1.mass- object2.mass)+ 2*object2.mass*object2.yVelocity) /(object1.mass + object2.mass)
    v2 = (object2.yVelocity+ (object2.mass- object1.mass)+ 2*object1.mass*object1.yVelocity) /(object1.mass + object2.mass)
    object1.yVelocity = v1
    object2.yVelocity = v2
def dynamicCollision(object1, object2):
    overlap = rectangleOverlap(object1.pos, object2.pos)
    plane ="o"
    if overlap:
        plane = lineCollide(object1.pos, object2.pos)
    if plane == "x":
        xDynamic(object1, object2)
    elif plane == "y":
        yDynamic(object1, object2)
    #(u1*m1) + (u2*m2) = v1*m1+v2*m2, (u1**2*m1) + (u2**2*m2) = (v1**2 * m1)+(v2**2 * m2)
    #u1 + u2 = v1 + v2, u1**2 + u2**2 = v1**2 + v2**2

    #v1 = (u1*(m1-m2)+2*m2*u2 ) / (m1 + m2)
    #v2 = (u2*(m2-m1)+2*m1*u1 ) / (m1 + m2)




