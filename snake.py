from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.head = self.whole_snake[0]

    def create_snake(self):
        dis = 20
        pos = 0
        for _ in range(0, 3):
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(x=pos, y=0)
            pos = pos - dis
            self.whole_snake.append(snake_segment)

    def move(self):
        for snake_segment in range(len(self.whole_snake) - 1, 0, -1):
            new_x = self.whole_snake[snake_segment - 1].xcor()
            new_y = self.whole_snake[snake_segment - 1].ycor()
            self.whole_snake[snake_segment].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def grow(self):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        new_x = self.whole_snake[-1].xcor()
        new_y = self.whole_snake[-1].ycor()
        snake_segment.goto(x=new_x, y=new_y)
        self.whole_snake.append(snake_segment)
