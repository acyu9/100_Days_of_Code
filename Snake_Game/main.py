from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Game window setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn tracer off
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    # Update screen with the snake as a whole instead of segment by segment the first loop
    # Subsequent loop updates after all segments have moved forward so shows up as the whole snake moved
    screen.update()
    # Snake moves at relative speed
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    no_head = snake.snake[1:]
    for segment in no_head:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

    screen.listen()
    screen.onkeypress(fun=snake.up, key="Up")
    screen.onkeypress(fun=snake.down, key="Down")
    screen.onkeypress(fun=snake.left, key="Left")
    screen.onkeypress(fun=snake.right, key="Right")

screen.exitonclick()