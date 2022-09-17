from turtle import Turtle
from random import randrange

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.start_angle()
        self.move_speed = 0.4

    def start_angle(self):
        angle = randrange(0, 360, 30)
        # Avoid straight y angles
        if angle == 90 or angle == 270:
            angle += 30
        self.setheading(angle)
    
    def bounce_wall(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)
    
    def bounce_paddle(self):
        new_heading = self.heading() + 90
        self.setheading(new_heading)
        self.move_speed *= 1.05

    def move(self):
        self.forward(self.move_speed)

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.3
        self.start_angle()
