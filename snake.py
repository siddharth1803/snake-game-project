from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.set_position()
        self.head = self.segments[0]

    def set_position(self):

        for position in STARTING_POSITION:
            self.add_segment(position)

    def move_snake(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.pensize(3)
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
