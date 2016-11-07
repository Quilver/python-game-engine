def stop(objectM, phase):
    if phase == "x":
        objectM.xVelocity = 0
        objectM.tempXv = 0
    else:
        objectM.yVelocity = 0
        objectM.tempYv = 0
def bounce(objectM, phase):
    if phase == "x":
        objectM.xVelocity *= -1
        objectM.tempXv *= -1
    else:
        objectM.yVelocity = 0
        objectM.tempYv = 0
def shove(object1, object2, phase):
    if phase == "x":
        if abs(object1.xVelocity)>abs(object2.xVelocity):
            if object1.xVelocity != object2.xVelocity:
                object2.xVelocity = object1.xVelocity
                object2.tempXv = object1.tempXv
    else:
        if abs(object1.yVelocity)>abs(object2.yVelocity):
            if object1.yVelocity != object2.yVelocity:
                object2.yVelocity = object1.yVelocity
                object2.tempYv = object1.tempYv

def losslessCollision(object1, object2, phase):
    #E=(mV^2)/2, p = m*v
    if phase == "x":
        object1.xVelocity = (object1.xVelocity*object1.mass + object2.xVelocity*object2.mass)/(object1.mass+object2.mass)
        object2.xVelocity = object1.xVelocity
        object1.tempXv = (object1.tempXv*object1.mass + object2.tempXv*object2.mass)/(object1.mass+object2.mass)
        object2.tempXv = object1.tempXv
    else:
        object1.yVelocity = (object1.yVelocity*object1.mass + object2.yVelocity*object2.mass)/(object1.mass+object2.mass)
        object2.yVelocity = object1.yVelocity
        object1.tempYv = (object1.tempYv*object1.mass + object2.tempYv*object2.mass)/(object1.mass+object2.mass)
        object2.tempYv = object1.tempYv