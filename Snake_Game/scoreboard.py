from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.point = 0
        self.score()
            
    def score(self):
        self.clear()
        self.write(arg=f"Score: {self.point}", align=ALIGNMENT, font=FONT)
        self.point += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
        