import sys

def collision(pos, momentum, y):
#stops the player from breaking moving through walls
    if pos[2]>=900 and momentum>0:
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
def hCollideBlock(dynamic, block, momentum, y):
    if (dynamic[2]>=block[0]) and (dynamic[0]<=block[2]):
            if (dynamic[3]>=block[1]) and (dynamic[1]<=block[3]):
                print("X")
                return momentum*-0.8, y
    return False, False

def vCollideBlock(dynamic, block, momentum, y):
    #this bit works...
    if (dynamic[3]>=block[1]) and (dynamic[1]<=block[3]):
        print("A")
        #this bit doesn't
        if (dynamic[2]<=block[0]-10) and (dynamic[0]>=block[2]+10):
            print("Y")
            return momentum, y*-0.4
    return False, False

def collider(dynamic, staticList, momentum, y):
    for i in range(len(staticList)):
        block=staticList[i]
        xCollide=hCollideBlock(dynamic, block, momentum, y)
        if xCollide[0]:
            return xCollide
        yCollide=vCollideBlock(dynamic, block, momentum, y)
        if yCollide[1]:
            return yCollide
    #print("Z")
    return momentum, y