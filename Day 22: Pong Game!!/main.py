from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 550)
screen.title("PONG!!")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
l_score = Scoreboard((-100, 170))
r_score = Scoreboard((100, 170))

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


playing = True
while playing:
    time.sleep(ball.delay)
    ball.move()
    screen.update()

    # Detect wall collision
    if abs(ball.ycor()) > 260:
        ball.wall_bounce()

    # Detect paddle collision
    if abs(ball.xcor()) > 350:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.paddle_bounce()

    # Detect right paddle miss
    if ball.xcor() > 370:
        l_score.win_point()
        ball.reset_position()

    # Detect left paddle miss
    if ball.xcor() < -370:
        r_score.win_point()
        ball.reset_position()



screen.exitonclick()
