from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.setposition(0, 0)
        self.y_direction = +10
        self.x_direction = +15

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_direction *= -1

    def bounce_paddle(self):
        self.x_direction *= -1




