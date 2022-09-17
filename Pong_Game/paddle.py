from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)
    
    def up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)
    
    def down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
    
    def top_cap(self):
        self.goto(self.xcor(), 250)
    
    def bottom_cap(self):
        self.goto(self.xcor(), -250)