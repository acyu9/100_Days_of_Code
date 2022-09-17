from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
# GUI textbox
choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
turtle_list = []

# Create a new object every loop with the following attributes, so ok to use the same name
for turtle in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y)
    new_turtle.color(colors[turtle])
    y += 40
    turtle_list.append(new_turtle)

is_race_on = False
# Race doesn't start until user made a choice
if choice:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        # Check if any turtle reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        steps = randint(0, 10)
        turtle.forward(steps)

screen.exitonclick()