from turtle import Turtle

FONT = ("Small Fonts", 50, 'normal')
class Scoreboard(Turtle):
    def __init__(self, location):
        super().__init__()
        self.draw_line()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(location)
        self.write(f"{self.score}", False,"center", FONT)


    def win_point(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False,"center", FONT)


    def draw_line(self):
        line = Turtle("square")
        line.color("white")
        line.shapesize(stretch_wid=.75, stretch_len=0.25)
        y_cor = 250
        while y_cor > -250:
            line.teleport(0, y_cor)
            line.stamp()
            y_cor -= 27

