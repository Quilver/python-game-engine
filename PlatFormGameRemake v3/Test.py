import dynamicObjects

def rectangleOverlap(dynamic, block):
    if (dynamic[2]>=block[0]) and (dynamic[0]<=block[2]):
        if (dynamic[3]>=block[1]) and (dynamic[1]<=block[3]):
            return True
    return False
s = rectangleOverlap([600.0, 600.0, 660.0, 700.0], [661.0, 599.0, 681.0, 639.0])
print(s)

def phaseDetection(posx, posy, deltax, delaty, block):
    plane = "o"
    if deltax>0 or 0<delaty:
        x= False
        y= False
        if rectangleOverlap(posx, block):
            x = True
        if rectangleOverlap(posy, block):
            y = True
        if x and y:
            if deltax<delaty:
                plane = "x"
            else:
                plane = "y"
        elif x:
            plane = "x"
        elif y:
            plane = "y"
    elif deltax>0:
        if rectangleOverlap(posx, block):
            plane = "x"
    elif delaty>0:
        if rectangleOverlap(posy, block):
            plane = "y"
    else:
        if abs(deltaX)>abs(Xvelocity) or abs(deltaY)>abs(Yvelocity):
            print("ErroR")
            quit()
    return plane