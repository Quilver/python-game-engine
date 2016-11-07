#Tracing list:
#star->pairTest->compair->update
#pairtest->detectPhase, detectPhase->distance
#node functions: start, pairTest
#leaf functions: compair, update, distance
def start(dynamicList, staticList):
    Frame = 0
    while Frame<1:
        pair = []
        pairs = 0
        TIME = 1
        for index in range(len(dynamicList)):
            object1 = dynamicList[index]
            if len(dynamicList)>1:
                for i in range(index+1, len(dynamicList)):
                    frame = pairTest(object1, dynamicList[i])
                    TIME, pairs, pair = compair(frame, TIME, pair, pairs)
            for i in staticList:
                frame = pairTest(object1, i)
                TIME, pairs, pair = compair(frame, TIME, pair, pairs)
        update(dynamicList, staticList, TIME, pair, pairs)
        Frame, pairs, pair = TIME, 0 ,[]
    for i in dynamicList:
        i.tempXv, i.tempYv = i.xVelocity, i.yVelocity

def compair(frame, TIME, pair, pairs):
    if frame[0]<TIME:
        TIME = frame[0]
        pair, pairs = [], 1
        pair.append([frame[1], frame[2], frame[3]])
    elif frame[0] == TIME:
        pairs += 1
        pair.append([frame[1], frame[2], frame[3]])
    return TIME, pairs, pair

def pairTest(object1, object2):
    x, y = detectPhase(object1, object2, "x"), detectPhase(object1, object2, "y")
    if x[0]<y[0]:
        return x
    else:
        return y


def detectPhase(object1, object2, plane):
    delta = distance(object1, object2, plane)
    if plane == "x":
        velocity = object1.tempXv - object2.tempXv
        velocity1, velocity2 = object1.tempYv, object2.tempYv
        point1, point2 = [object1.pos[1], object1.pos[3]], [object2.pos[1], object2.pos[3]]
    elif plane == "y":
        velocity = object1.tempYv - object2.tempYv
        velocity1, velocity2 = object1.tempXv, object2.tempXv
        point1, point2 = [object1.pos[0], object1.pos[2]], [object2.pos[0], object2.pos[2]]
    if velocity!=0:
        time = delta / velocity
    else:
        return 2, object1, object2, "o"
    point1[0] += time*velocity1
    point1[1] += time*velocity1
    point2[0] += time*velocity2
    point2[1] += time*velocity2
    if (time>=0) and (1 >= time):
        if (point1[1] >point2[0]) and (point1[0] < point2[1]):
            return time, object1, object2, plane
    return 2, object1, object2, "o"

def distance(object1, object2, plane, type = "rectangle"):
    if plane == "x":
        points1 = object1.pos[0], object1.pos[2]
        v1 = object1.tempXv
        points2 = object2.pos[0], object2.pos[2]
        v2 = object2.tempXv
    elif plane == "y":
        points1 = object1.pos[1], object1.pos[3]
        v1 = object1.tempYv
        points2 = object2.pos[1], object2.pos[3]
        v2 = object2.tempYv
    if (points1[1] > points2[0]) and (points1[0] < points2[1]):
        delta = -(v1-v2)
    elif (v1-v2) > 0:
        delta = points2[0]-points1[1]
    else:
        delta = -(points1[0]-points2[1])
    return delta

def update(dynamicList, staticList, timeFrame, pair, pairs):
    #list of pair = [object1, object2, phase]
    #pairs how many pair there are
    for i in dynamicList:
        i.move(i.tempXv, i.tempYv, timeFrame)
        i.tempXv -= i.tempXv*timeFrame
        i.tempYv -= i.tempYv*timeFrame
    if pairs>=1:
        for i in pair:
            i[0].act(i[1], i[2])
            i[1].act(i[0], i[2])
