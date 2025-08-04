###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]



turtle.colormode(255)

tim = turtle.Turtle()
tim.teleport(-200, -200)
x = tim.xcor()
y = tim.ycor()
starting_x = x
print(f"X coord: {x}, Y coord: {y}")
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        x += 70
        tim.teleport(x, y)
    x = starting_x
    y += 70
    tim.teleport(x, y)

screen = turtle.Screen()
screen.exitonclick()