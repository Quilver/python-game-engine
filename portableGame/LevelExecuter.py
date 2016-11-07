import time, sys, dynamicObjects, os
from assets.parents import Graphics as Graphics
#from GameAssets import*
def gameAssets(list, directory = "assets"):
    import glob, os, sys
    os.chdir(directory)
    for file in glob.glob("*.py"):
        print(file)
        module = file
        module = os.path.splitext(module)[0]
        assets.append(module)
    os.chdir(os.pardir)
assets =[]
gameAssets(assets, "assets")
print(assets)
for asset in assets:
    importString = "from " + "assets." + asset + " import*"
    print(importString)
    exec(importString)



def areaReader(level, engine, canvas):
    fileName="area"+str(level)+".txt"
    fileName = os.path.join("area", fileName)
    MAP = open(fileName, "r")
    #MAP=open(fileName, 'r')
    for line in MAP:
        exec(str(line))
    MAP.close()

def main(canvas= Graphics.GraphicsEngine()):
    #setting up engines
    FPS = 1/60
    engine = dynamicObjects.PhysicsEngine(FPS, drag = 0, Gforce = 0)
    #sets up level
    level = 1
    while level <= 3:
         #sets up new level
        hasNotWon=True
        areaReader(level, engine, canvas)
         #run game loop
        while hasNotWon:
            deltaFps = time.time()
            canvas.draw()
            ##print("graphics", int(1/(time.time()-deltaFps) ))
             #runs all game logic per frame
            ##p = time.time()
            hasNotWon = engine.proccess()
            ##print("physics", int(1/(time.time()-p) ))
            deltaFps-= time.time()
            deltaFps *= -1
            if deltaFps<FPS:
                time.sleep(FPS-deltaFps)
            ##if deltaFps!=0:
            ##    print("Frame", int(1/deltaFps))
        level+=1
        canvas.reset()
        engine.reset()
    #shuts down window after game is finished
    Graphics.terminate()


main()