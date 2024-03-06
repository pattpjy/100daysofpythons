# Turtle Intro

import turtle as t
import random
pimmy_the_turtle = t.Turtle()
#
# for _ in range(4):
#     pimmy_the_turtle.forward(100)
#     pimmy_the_turtle.left(90)

# for _ in range(15):
#     pimmy_the_turtle.forward(10)
#     pimmy_the_turtle.penup()
#     pimmy_the_turtle.forward(10)
#     pimmy_the_turtle.pendown()


colors = ['red', 'orange', 'blue', 'green', 'brown', 'DeepSkyBlue', 'pink', 'yellow']


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         pimmy_the_turtle.forward(100)
#         pimmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     pimmy_the_turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)

# create random color
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    # store rbg number in tuple
    color_random = (r, g, b)
    return color_random


# draw random walk


# directions = [0, 90, 180, 270]
# pimmy_the_turtle.pensize(15)

# for _ in range(200):
#     # # get color from color array
#     # pimmy_the_turtle.color(random.choice(colors))
#     pimmy_the_turtle.color(random_color())
#     pimmy_the_turtle.forward(30)
#     pimmy_the_turtle.setheading(random.choice(directions))


# drawing circle spirograph
pimmy_the_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        pimmy_the_turtle.color(random_color())
        pimmy_the_turtle.circle(size_of_gap)
        pimmy_the_turtle.setheading(pimmy_the_turtle.heading() + size_of_gap)


draw_spirograph(30)
screen = t.Screen()
screen.exitonclick()

