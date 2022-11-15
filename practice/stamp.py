import turtle

WIDTH = 600
HEIGHT = 600
SCREEN_TITLE = "Screen Title"
SCREEN_BGCOLOR = "blue"

screen = turtle.Screen()

# Screen config
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(SCREEN_BGCOLOR)
screen.title(SCREEN_TITLE)

# Stamper
stamper = turtle.Turtle()
stamper.shape("turtle")
stamper.color("violet")
stamper.shapesize(50/20)
stamper.stamp()

stamper.penup()
stamper.goto(100, 100)

stamper.shapesize(10/20)
stamper.stamp()

stamper.shapesize(200/20)
stamper.penup()
stamper.goto(-150, -100)

# Finish
turtle.done()
