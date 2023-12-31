from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SEGMENT_DISTANCE = 20
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            next_x = self.snake_segments[segment_num - 1].xcor()
            next_y = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(next_x, next_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()

        self.create_snake()
        self.head = self.snake_segments[0]
