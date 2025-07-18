from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle:
    def __init__(self, starting_positions):
        self.segments = []
        self.create_paddle(starting_positions)

    # TODO 2 : Create the paddle
    def create_paddle(self, starting_positions):
        for position in starting_positions:
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
