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
        self.score = 0
        with open("score.txt") as file:
            self.highest_score = int(file.read())
        self.update_score()
            
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_score()
        