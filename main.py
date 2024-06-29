# import turtle
from turtle import Turtle, Screen
# import random


# tim = Turtle()
# tim.shape("turtle")
# tim.color("green", "red")

# for _ in range(4):
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.right(90)
# colours = ["dark green", "teal", "dark red", "dark orange", "yellow green",
#            "lime", "deep pink", "green yellow", "indian red"]


# Directions = [0, 90, 180, 260]
# tim.pensize(20)
# tim.speed("fastest")
# turtle.colormode(255)

# def shape(num_sides):
#     for _ in range(num_sides):
#         angel = 360 / num_sides
#         tim.forward(100)
#         tim.right(angel)
#
# for shape_of_the_shapes in range(3, 11):
#     shape(shape_of_the_shapes)
#     tim.color(random.choice(colours))
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(40)
#     tim.setheading(random.choice(Directions))


# screen = Screen()
# screen.exitonclick()



# SPIROGRAPH

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

