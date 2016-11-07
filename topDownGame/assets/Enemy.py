import inherit.Dynamic as dynamicObjects
class Enemy(dynamicObjects.Dynamic):
    def draw(self):
        self.xVelocity = -5
        self.name = "dynamic"
        if self.colour ==(100, 250, 100):
            self.id = self.canvas.create_image("brick.jpg", self.x, self.y, self.width, self.length)
        else:
            self.id = self.canvas.create_rectangle(self.colour, [self.x, self.y, self.width, self.length])
        self.pos = [self.x, self.y, self.x+self.width, self.x+self.length]
    def update(self):
        self.xVelocity += 0.06
        self.yVelocity /= 1.1
    def act(self, objectM, phase):
        if objectM.name == "player" or "dynamic" == objectM.name:
            shove(self, objectM, phase)
