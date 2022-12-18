from turtle import Turtle
from random import choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.left(180)
        self.color(choice(COLORS))
        self.penup()
        self.move_speed = 5
        self.initial_cars()        
        
    def initial_cars(self):
        initial_position = randrange(-250, 250, 20)
        self.goto(initial_position, initial_position)
    
    def new_cars(self):
        self.color(choice(COLORS))
        self.goto(300, randrange(-250, 250, 20))

    def move(self):
        self.forward(self.move_speed)
    
    def next_level(self):
        self.move_speed += 5