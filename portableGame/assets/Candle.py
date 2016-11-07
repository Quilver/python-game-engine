class Candle():
    def __init__(self, engine, canvas, x, y):
        self.x, self.y = x, y
        self.width, self.length = 20, 20
        self.canvas = canvas
        self.id = self.canvas.create_image("candle.png", self.x, self.y, self.width, self.length)
        engine.background.append(self)
    def move(self, xVelocity, yVelocity, timeFrame =1):
        self.canvas.move_image(self.id, int(xVelocity*timeFrame), int(yVelocity*timeFrame))