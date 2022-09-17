from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()


def move_forward():
    timmy_the_turtle.forward(10)  


def move_backward():
    timmy_the_turtle.backward(10)


def move_cw():
    timmy_the_turtle.right(10)


def move_ccw():
    timmy_the_turtle.left(10)


def clear():
    screen.resetscreen()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_cw, key="d")
screen.onkey(fun=move_ccw, key="a")
screen.onkey(fun=clear, key="c")
screen.listen()

screen.exitonclick()