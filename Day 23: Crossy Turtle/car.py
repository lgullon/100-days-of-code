from turtle import Turtle

class Car(Turtle):
    def __init__(self, color, x_cor, y_cor, speed):
        super().__init__()
        self.speed = speed
        self.y_cor = y_cor

        self.shape("square")
        self.shapesize(1, 2)
        self.color(color)
        self.penup()
        self.goto(x_cor, y_cor)
        self.setheading(180)

    def move(self):
        self.forward(self.speed)