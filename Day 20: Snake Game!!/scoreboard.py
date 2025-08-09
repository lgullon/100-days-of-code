from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.teleport(0, 250)
        self.hideturtle()
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER.", False, ALIGNMENT, FONT)