from turtle import Turtle, Screen
import time
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.segments = list()
        self.create_snake()
        self.head = self.segments[0]



    def create_snake(self):
        # create snake
        start_x = 0
        for _ in range(3):
            self.add_segment((start_x, 0))
            start_x -= MOVE_DISTANCE



    def move(self):

        for seg_index in range(len(self.segments)-1, 0, -1):
            self.segments[seg_index].goto(self.segments[seg_index - 1].pos())

        self.head.forward(20)


    def add_segment(self, position):
        new_segment = Turtle("turtle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)