from turtle import Screen, Turtle
from score import Score
import pandas

# Set up background
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
background = Turtle()
background.shape(image)

score = 0
states = Score()
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
states_guessed = []

while score < 51:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    
    # Check if user wants to end game
    if answer_state == "Exit":
        break
    
    # Check if user input matches the states list, including spelling, and whether state guessed already
    if answer_state in states_list and answer_state not in states_guessed:
        row = data[data.state == answer_state]
        x_coor = int(row.x)
        y_coor = int(row.y)
        states.write_state(x_coor, y_coor, answer_state)
        score += 1
        states_guessed.append(answer_state)

# Find the states that are not guessed
states_to_learn = set(states_list).difference(states_guessed)
# Convert set to list to dictionary to DataFrame
data = pandas.DataFrame({"states": list(states_to_learn)})
data.to_csv("states_to_learn.csv")