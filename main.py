from turtle import Turtle, Screen
import random


# Build the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Classic Snake Game")

# Build the original body of the snake
dis = 20
pos = 0
whole_snake = []
for _ in range(0,3):
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.goto(x=pos, y=0)
    pos = pos - dis

screen.exitonclick()