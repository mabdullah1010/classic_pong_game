import turtle


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.goto(350, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 30)








