import time, sys, dynamicObjects, Graphics
from GameAssets import*

#setting up engines
FPS = 1/60
engine = dynamicObjects.PhysicsEngine(FPS, drag = 0, Gforce = 0)
canvas = Graphics.GraphicsEngine()
def areaReader(level):
    fileName="area"+str(level)+".txt"
    MAP=open(fileName, 'r')
    for line in MAP:
        exec(str(line))
    MAP.close()

#sets up level
level = 1
while level <= 3:
     #sets up new level
    hasNotWon=True
    areaReader(level)
     #run game loop
    while hasNotWon:
        deltaFps = time.time()
        canvas.draw()
         #runs all game logic per frame
        hasNotWon = engine.proccess()
         #updates the graphics each frame
        #Graphics.playerInput(engine.player)
        deltaFps-= time.time()
        deltaFps *= -1
        #print(deltaFps)
        if deltaFps<FPS:
            time.sleep(FPS-deltaFps)
        #if deltaFps!=0:
        #    print(int(1/deltaFps))
    level+=1
    canvas.reset()
    engine.reset()
#shuts down window after game is finished
Graphics.terminate()