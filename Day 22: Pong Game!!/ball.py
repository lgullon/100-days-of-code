from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.delay = 0.05

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y *= -1

    def paddle_bounce(self):
        self.x *= -1
        self.delay *= 0.9

    def reset_position(self):
        self.teleport(0, 0)
        self.paddle_bounce()
        self.delay = 0.05