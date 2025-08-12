import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle!!")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
loop_count = 0
car_speed = 8
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loop_count % car_speed == 0:
        car_manager.new_car()

    # this loop moves the cars and checks for collisions
    for car in car_manager.cars:
        car.move()
        if player.distance(car) < 25:
            game_is_on = False
            screen.update()
            scoreboard.game_over()

    # player passes finish line
    if player.ycor() > 290:
        scoreboard.next_level()
        player.reset()
        car_manager.increase_speed()
        car_speed /= 2




    loop_count += 1

screen.exitonclick()
