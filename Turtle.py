from turtle import Turtle, Screen
from random import choice, randint

# Create object of Turtle class
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("purple")

# Draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# Draw dashed line
# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


# # Draw multiple shapes, sharing one side
# colors = ["blue", "green", "red", "black", "cyan"]
# color = 0
# sides = 3

# while sides < 9:
#     each_angle = 360 / sides
#     for i in range(sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(each_angle)
#     sides += 1
#     # Could use random.choice too
#     timmy_the_turtle.color(colors[color])
#     if color < 4:
#         color += 1


# Random walk with thicker pen, different color, faster speed
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


screen = Screen()
# Set the colormode to between 0 and 255
screen.colormode(255)
# timmy_the_turtle.pensize(9)
timmy_the_turtle.speed("fastest")
# directions = [0, 90, 180, 270]

# for i in range(40):
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.right(choice(directions))
#     timmy_the_turtle.color(random_color())


# Draw a spirograph with different color and circle of radius 100
# 360 / 5 = 72 circles to make a full circle
for i in range(72):
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(5)
    timmy_the_turtle.color(random_color())

screen.exitonclick()
