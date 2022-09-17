from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Game Screen Setting
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Ensures the paddles don't go off the screen
    if left_paddle.ycor() > 250:
        left_paddle.top_cap()
    elif left_paddle.ycor() < -250:
        left_paddle.bottom_cap()
    elif right_paddle.ycor() > 250:
        right_paddle.top_cap()
    elif right_paddle.ycor() < -250:
        right_paddle.bottom_cap()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # Detect collision with the paddles
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    
    # Detect ball going off screen
    if ball.xcor() > 420:
        score.update_left()
        ball.reset()
    elif ball.xcor() < -420:
        score.update_right()
        ball.reset()

screen.exitonclick()