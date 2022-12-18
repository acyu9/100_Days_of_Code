from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def write_state(self, x_coor, y_coor, state):
        self.goto(x_coor, y_coor)
        self.write(arg=state, align="left", font=("Courier", 8, "normal"))
