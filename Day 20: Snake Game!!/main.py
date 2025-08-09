from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        playing = False
        scoreboard.game_over()

    # Detect tail collision
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            playing = False
            scoreboard.game_over()




screen.exitonclick()


