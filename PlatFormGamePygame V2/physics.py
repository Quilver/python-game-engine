import sys
import copy
def quit():
    sys.exit()
def rounded(number):
    num = number
    num -= int(number)
    if num>=0.5:
        num = 1
    else:
        num = 0
    return int(number)+num
#collision detection for the camera if I want this to be a side scroller
def cameraCollision(pos, momentum, y):
#stops the player from breaking moving through walls
    pass
def rectangleOverlap(dynamic, block):
    if (dynamic[2]>=block[0]) and (dynamic[0]<=block[2]):
        if (dynamic[3]>=block[1]) and (dynamic[1]<=block[3]):
            return True
    return False
#bounding box collisions
def Broad(pos, staticList, Xvelocity, Yvelocity):
    Collisions = []
    if (Xvelocity!=0) or (Yvelocity!=0):
        if Xvelocity!=0:
            if Xvelocity>0:
                Box = [pos[2], pos[1], pos[2]+Xvelocity, pos[3]]
            else:
                Box = [pos[0]+Xvelocity, pos[1], pos[0], pos[3]]
        else:
            if Yvelocity>0:
                Box = [pos[0], pos[3], pos[2], pos[3]+Yvelocity]
            else:
                Box = [pos[0], pos[1]+Yvelocity, pos[2], pos[1]]
    else:
        return []
    for i in staticList:
        if rectangleOverlap(Box, i.pos):
            Collisions.append(i)
    return Collisions

def broadPhase(pos, staticList, Xvelocity, Yvelocity):
    Collisions = []
    if (Xvelocity==0) or (Yvelocity==0):
        return Broad(pos, staticList, Xvelocity, Yvelocity)
    elif Xvelocity > 0:
        Xbox = [pos[2], pos[1], pos[2]+Xvelocity, pos[3]]
        if Yvelocity > 0:
            Ybox = [pos[0], pos[3], pos[2], pos[3]+Yvelocity]
            Box = [pos[2], pos[3], pos[2]+Xvelocity, pos[3]+Yvelocity]
        else:
            Ybox = [pos[0], pos[1]+Yvelocity, pos[2], pos[1]]
            Box = [pos[2], pos[1]+Yvelocity, pos[2]+Xvelocity, pos[1]]
    else:
        Xbox = [pos[0]+Xvelocity, pos[1], pos[0], pos[3]]
        if Yvelocity > 0:
            Ybox = [pos[0], pos[3], pos[2], pos[3]+Yvelocity]
            Box = [pos[0]+Xvelocity, pos[3], pos[0], pos[3]+Yvelocity]
        else:
            Ybox = [pos[0], pos[1]+Yvelocity, pos[2], pos[1]]
            Box = [pos[0]+Xvelocity, pos[1]+Yvelocity, pos[0], pos[1]]

    for i in staticList:
        if rectangleOverlap(Xbox, i.pos) or rectangleOverlap(Ybox, i.pos) or rectangleOverlap(Box, i.pos):
            Collisions.append(i)
    return Collisions

def moveBox(pos, Xvelocity, Yvelocity, deltaX, deltaY):
    posX = copy.deepcopy(pos)
    posY = copy.deepcopy(pos)
    if Xvelocity < 0:
        deltaX *= -1
    if Yvelocity < 0:
        deltaY *= -1
    if Xvelocity!=0:
        posX[0] += deltaX
        posX[2] += deltaX
        posX[1] += Yvelocity * abs(deltaX/Xvelocity)
        posX[3] += Yvelocity * abs(deltaX/Xvelocity)
    #PosY
    if Yvelocity!=0:
        posY[1] += deltaY
        posY[3] += deltaY
        posY[0] += Xvelocity * abs(deltaY/Yvelocity)
        posY[2] += Xvelocity * abs(deltaY/Yvelocity)
    return posX, posY
#finds the distance between two squares on the x and y planes
def deltaSquare(Xvelocity, Yvelocity, square1, square2):
    if (Xvelocity>0):
        deltaX = square2[0] - square1[2]
    else:
        deltaX = square1[0] - square2[2]
    if (Yvelocity>0):
        deltaY = square2[1] - square1[3]
    else:
        deltaY = square1[1] - square2[3]
    return deltaX, deltaY
def narrowPhaseCollisions(dynamic, staticList, Xvelocity, Yvelocity, TimeList, Phase):
    #firstCollision = static[len(static)-1- TimeList.index(min(TimeList))]
    #print(TimeList)
    counter=0
    for i in TimeList:
        if i!=101.101:
            counter+=1
            if abs(i)>1:
                print("288: WTF somthings wrong")
    if counter > 0:
        index = TimeList.index(min(TimeList))
        deltaX = min(TimeList)*Xvelocity
        deltaY = min(TimeList)*Yvelocity
        dynamic.move(deltaX, deltaY)

        if Xvelocity>0:
            Xvelocity = abs(Xvelocity)-abs(deltaX)
        else:
            Xvelocity = -(abs(Xvelocity)-abs(deltaX))

        if Yvelocity>0:
            Yvelocity = abs(Yvelocity)-abs(deltaY)
        else:
            if abs(deltaY)>20:
                print(deltaY, " 3")
                quit()
            Yvelocity = -(abs(Yvelocity)-abs(deltaY))
        if Phase[index] == "x":
            Xvelocity *= -1
            if abs(dynamic.xVelocity)>3:
                dynamic.xVelocity *= -1
            else:
                dynamic.xVelocity = 0
        else:
            Yvelocity *= -1
            if abs(dynamic.yVelocity)>3:
                dynamic.yVelocity *= -1
            else:

                dynamic.yVelocity = 0
        boundingBoxTest(dynamic, staticList, rounded(Xvelocity), rounded(Yvelocity))
    else:
        dynamic.move(Xvelocity, Yvelocity)

def phaseDetection(posx, posy, deltax, deltay, block, xvelocity, yvelocity):
    plane = "o"
    if (deltax>=0 and 0<=deltay):# and (xvelocity!=0 or yvelocity!=0):
        x= False
        y= False
        if rectangleOverlap(posx, block):
            x = True
        if rectangleOverlap(posy, block):
            y = True
        if x and y:
            if deltax<deltay:
                plane = "x"
            else:
                plane = "y"
        elif x:
            plane = "x"
        elif y:
            plane = "y"
    elif deltax>=0 and xvelocity!=0:
        if rectangleOverlap(posx, block):
            plane = "x"
    elif deltay>=0 and yvelocity!=0:
        if rectangleOverlap(posy, block):
            plane = "y"

    return plane

def medPhaseCollisions(dynamic, staticList, Xvelocity, Yvelocity):
    dynamic.move(0,0)
    TimeList = []
    Phase = []
    pos = dynamic.pos
    for i in range(0, len(staticList)):
        deltaX, deltaY = deltaSquare(Xvelocity, Yvelocity, pos, staticList[i].pos)
        posX, posY = moveBox(pos, Xvelocity, Yvelocity, deltaX, deltaY)
        phase = phaseDetection(posX, posY, deltaX, deltaY, staticList[i].pos, Xvelocity, Yvelocity)
        if phase=="x":
            Phase.append("x")
            if Xvelocity!=0:
                TimeList.append(deltaX/abs(Xvelocity))
            else:
                TimeList.append(0)
        elif phase=="y":
            Phase.append("y")
            if Yvelocity!=0:
                TimeList.append(deltaY/abs(Yvelocity))
            else:
                TimeList.append(0)
        else:
            Phase.append("o")
            TimeList.append(101.101)

    for i in TimeList:
        if (i>1 or i<0) and (i!=101.101):
            print("error", i)
            quit()
    narrowPhaseCollisions(dynamic, staticList, Xvelocity, Yvelocity, TimeList, Phase)


def boundingBoxTest(dynamic, staticList, Xvelocity = "a", Yvelocity = "a"):
    pos = dynamic.pos
    if Xvelocity == "a":
        Xvelocity = dynamic.xVelocity
        #print(Xvelocity, "X")
    if Yvelocity == "a":
        Yvelocity = dynamic.yVelocity
        #print(Yvelocity, "Y")
    #TESTBOX = [pos[2], pos[3], pos[2] + Xvelocity, pos[3] + Yvelocity]
    Collisions = broadPhase(pos, staticList, Xvelocity, Yvelocity)
    #for i in staticList:
    #    if rectangleOverlap(TESTBOX, i.pos):
    #        Collisions.append(i)
    if len(Collisions)>0:
        '''if Xvelocity==0 or Yvelocity==0:
            if Xvelocity !=0:
                dynamic.xVelocity*=-1
                dynamic.move(Xvelocity, 0)
            else:
                dynamic.yVelocity*=-1
                dynamic.move(0, Yvelocity)
        else:'''
        medPhaseCollisions(dynamic, Collisions, Xvelocity, Yvelocity)
    else:
        dynamic.move(Xvelocity, Yvelocity)






