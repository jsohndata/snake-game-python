import turtle
import random

# Define program constants
WIDTH = 800
HEIGHT = 600
DELAY =  100 # Miliseconds between screen updates.
GAME_NAME = "đ đšī¸ Snake Game"
GAME_BGCOLOR = "#131313"
SNAKE_SHAPE = "circle"
SNAKE_COLOR = "#9820C5"
FOOD_SHAPE = "triangle"
FOOD_COLOR = "#F0C32E"
FOOD_SIZE = 20

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def game_loop(): 
    stamper.clearstamps() # Remove all the stamps.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake \
        or new_head[0] < - WIDTH / 2 \
        or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 \
        or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # Append new head to snake body.
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Draw snake for the first time.
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh screen
        screen.title(f"{GAME_NAME}. Score: {score}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score

    if get_distance(snake[-1], food_pos) < 20:
        score += 1 
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorem
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    game_loop()


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title(GAME_NAME)
screen.bgcolor(GAME_BGCOLOR)
screen.tracer(0)  # Turn off automatic animation.

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape(SNAKE_SHAPE)
stamper.color(SNAKE_COLOR)
stamper.penup()

# Create snake as a list of coordinate pairs.
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"
score = 0


# Food
food = turtle.Turtle()
food.shape(FOOD_SHAPE)
food.color(FOOD_COLOR)
food.shapesize(FOOD_SIZE / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

# Set animation in motion
reset()

turtle.done()