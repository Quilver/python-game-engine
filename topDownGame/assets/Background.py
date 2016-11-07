class Background():
    def __init__(self, engine, canvas):
        self.x, self.y = -500, -500
        self.width, self.length = 2000, 2000
        self.canvas = canvas
        self.id = self.canvas.create_image("background.png", self.x, self.y, self.width, self.length)
        engine.background = self
    def move(self, xVelocity, yVelocity, timeFrame =1):
        self.canvas.move_image(self.id, int(xVelocity*timeFrame/2), int(yVelocity*timeFrame/2))