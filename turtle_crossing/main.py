import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NUM_OF_CARS = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

# Create initial cars and add to list
car_total = []
for i in range(NUM_OF_CARS):
    car = CarManager()
    car_total.append(car)

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Go through list of cars to make each move and regenerate when moving off screen
    for car in car_total:
        car.move()
        if car.xcor() < -320:
            car.new_cars()
    
        # Detect collision between player and car
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    
    # Detect if player has won. If so, update level
    if player.ycor() > 270:
        player.next_level()
        scoreboard.update()
        for car in car_total:
            car.next_level()

screen.exitonclick()


# Could move more parts to the classes themselves so main is cleaner/shorter