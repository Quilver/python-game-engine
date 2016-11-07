class Circle():
    def __init__(self, x, y, radius, engine,  colour = "red", density = 10, dynamic = False):
        if dynamic:
            engine.dynamic.append(self)
        else:
            engine.static.append(self)
    def draw(self):
        pass
    def update(self):
        pass
    def move(self):
        pass