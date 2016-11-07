# This will be a math library
import math

#finds the distance between two points represented as tuples
def distanceBetweenTwoPoint(pos1, pos2):
    deltX=pos1[0]-pos2[0]
    deltaY=pos1[1]-pos2[1]
    dist=deltX**2+deltY**2
    return math.sqrt(dist)

#finds the attraction one object has to another based on distance, mass and force of the attraction
def attraction(obj1, obj2):
    pass
#identifier
def findXYOnACircle(radius, degrees):
    #code to be executed
    radians=math.radians(degrees)
    adjacent=radius*math.sin(radians)
    SquaredOpposite=radius**2-adjacent**2
    opposite=math.sqrt(SquaredOpposite)
    pos=(adjacent, opposite)
    #returning value
    return pos

#Bubble sort
def bubbleSort(list1D):
    size=len(list1D)-1
    size1=len(list1D)-1
    for i in range(size):
        swaps=True
        for y in range(size1):
            if list1D[y+1]<list1D[y]:
                temp=list1D[y+1]
                list1D[y+1]=list1D[y]
                list1D[y]=temp
                swaps=False
        size1-=1
        if swaps:break
    return list1D

#Depreciation
def deperciate(rounds, percentDrop, value):
    if rounds==1:
        return value
    else:
        rounds-=1
        value*=percentDrop
        return deperciate(rounds, percentDrop, value)

def fibbonachi(n):
    if n==1: return 1
    elif:n==2:
        return 1
    else: return (fibbonachi(n-1)+fibbonachi(n-2))

