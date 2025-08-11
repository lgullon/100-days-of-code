from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = list()

y_start = -75
for color in colors:
    turt = Turtle(shape="turtle")
    turt.color(color)
    turt.penup()
    turt.goto(x=-230, y=y_start)
    y_start += 30
    turtles.append(turt)

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=0)

is_racing = True
winner = None
while is_racing:

    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            is_racing = False
            winner = turtle
            if turtle.pencolor() == user_bet:
                print(f"You've won!! {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost.. {turtle.pencolor()} turtle is the winner!")


screen.exitonclick()
