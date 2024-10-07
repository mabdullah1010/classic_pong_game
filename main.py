import turtle
from paddle import Paddle
from ball import Ball
from walls import Wall
from score_board import ScoreBoard
import time
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(0.9, 0.9)
screen.screensize(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
score_1 = ScoreBoard((-100, 200))
score_2 = ScoreBoard((100, 200))

top_wall = Wall((0, 310))
bottom_wall = Wall((0, -310))


paddle2.goto(-350, 0)


screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    if ball.ycor() >= 300:
        ball.bounce_wall()
    elif ball.ycor() <= -300:
        ball.bounce_wall()

    if ball.xcor() >= 330 and ball.distance(paddle1) <= 50:
        ball.bounce_paddle()
    elif ball.xcor() <= -330 and ball.distance(paddle2) <= 50:
        ball.bounce_paddle()

    if ball.xcor() >= 370:
        score_1.clear()
        score_1.increase_score()
        ball.goto(0, 0)
        ball.move()

    elif ball.xcor() <= -370:
        score_2.clear()
        score_2.increase_score()
        ball.goto(0, 0)
        ball.move()

    if score_1.score >= 3 or score_2.score >= 3:
        game_is_on = False

if score_1.score > score_2.score:
    score_1.clear()
    score_1.write("Winner", False, "center", ("Arial", 15, "bold"))
    score_2.clear()
    score_2.write("Loser", False, "center", ("Arial", 15, "bold"))
else:
    score_2.clear()
    score_2.write("Winner", False, "center", ("Arial", 15, "bold"))
    score_1.clear()
    score_1.write("Loser", False, "center", ("Arial", 15, "bold"))

screen.exitonclick()
