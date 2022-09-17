# virtual environment command: python -m venv venv

import colorgram
from turtle import Turtle, Screen
from random import choice

colors = colorgram.extract('dots.jpg', 25)
color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    color_list.append(color_tuple)

#print(color_list)

color_list = [(238, 230, 235), (224, 162, 65), (18, 43, 84), (238, 229, 220), (135, 61, 85), 
    (227, 239, 233), (175, 61, 43), (126, 38, 60), (57, 48, 35), (21, 86, 61), (246, 196, 52), 
    (18, 114, 143), (195, 140, 160), (228, 85, 39), (56, 139, 72), (229, 173, 190), (154, 188, 179), 
    (194, 101, 133), (24, 64, 53), (58, 71, 38), (165, 204, 199), (68, 22, 42), (65, 155, 81), 
    (34, 44, 103)]

screen = Screen()
screen.colormode(255)

# Circle size 20, space 50, 10x10 size
timmy_the_turtle = Turtle()

# Set up the turtle - hide and starting location
timmy_the_turtle.hideturtle()
timmy_the_turtle.speed("fastest")
x = -230
y = -230


def location(x, y):
    """Move the turtle to the designated location without drawing"""
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x, y)
    timmy_the_turtle.pendown()


# Starting location
location(x, y)

for height in range(10):
    for row in range(10):
        # Draw dot
        timmy_the_turtle.dot(20, choice(color_list))

        # Leave gap between dots
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
        timmy_the_turtle.pendown()
    
    # Move up the row
    y += 50
    location(x, y)

screen.exitonclick()