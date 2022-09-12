import turtle

import colorgram
import random
from turtle import Turtle, Screen
tim = Turtle()
colors = colorgram.extract('hirst_painting.jpg', 1000)

color_list = [(244, 239, 226), (235, 243, 239), (194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15), (168, 208, 178), (14, 88, 104), (162, 203, 212), (220, 179, 173), (236, 204, 13)]

turtle.colormode(255)
def painting(x_rep, y_rep, list_of_colors):
    y_pos = -200
    tim.penup()
    tim.goto(-200, -200)
    for x_rep in range(10):
        for x_rep in range(10):
            color = random.choice(list_of_colors)
            tim.dot(20, color)
            tim.forward(50)
        y_pos += 50
        tim.goto(-200, y_pos)


painting(10, 10, color_list)

# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     tup = (r, g, b)
#     color_list.append(tup)
# print(color_list)
screen = Screen()
screen.exitonclick()
