from turtle import Turtle

# Constant
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
INITIAL_SEGMENTS = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # What happens when a new snake object is initialized
    def __init__(self):
        # Set up snake. Use self for class attribute
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.penup()
        snake_body.color("white")
        snake_body.goto(position)
        # Self to refer to attribute snake
        self.snake.append(snake_body)
    
    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def move(self):
        # start, stop, step
        for segment in range(len(self.snake)-1, 0, -1):
            # Move the 2nd segment to 1st segment's position, etc.
            new_position = self.snake[segment-1].position()
            self.snake[segment].goto(new_position)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        # Snake can't go back on itself
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)