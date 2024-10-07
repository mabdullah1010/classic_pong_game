from turtle import Turtle


class Wall(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(position)
        self.shapesize(1, 50)
