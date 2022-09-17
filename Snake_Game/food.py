from turtle import Turtle
from random import randrange

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # 10 x 10 circle (normally 20 x 20)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randrange(-200, 200, 20)
        random_y = randrange(-200, 200, 20)
        self.goto(random_x, random_y)