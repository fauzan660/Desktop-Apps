class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = y
        self.y = x
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.color


class Square:
    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color