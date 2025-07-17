from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (350, -20), (350, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    # TODO 2 : Create the paddle
    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

        # TODO 3 : Make the paddle move
    def paddle_up(self):
        for segment in self.segments:
            new_y = segment.ycor() + MOVE_DISTANCE
            segment.goto(segment.xcor(), new_y)

    def paddle_down(self):
        for segment in self.segments:
            new_y = segment.ycor() - MOVE_DISTANCE
            segment.goto(segment.xcor(), new_y)
