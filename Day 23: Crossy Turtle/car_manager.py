import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        for _ in range(12):
            y = random.randint(-8, 9) * 25
            x = random.randint(-250, 250)
            color = COLORS[random.randint(0, 5)]
            self.cars.append(Car(color, x, y, self.speed))


    def new_car(self):
        color = COLORS[random.randint(0, 5)]
        y_cor = random.randint(-8, 9) * 25
        self.cars.append(Car(color, 300, y_cor, self.speed))

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        for car in self.cars:
            car.speed = self.speed