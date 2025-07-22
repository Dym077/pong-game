from turtle import Turtle
import random as r
#TODO 4: Create the ball
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0.0)
        self.color("white")
        self.shape("circle")
        self.pu()
        self.x_move = 10
        self.y_move = 10

# TODO 5: Make the ball move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

# TODO 6: Make the ball bounce
    def bounce(self):
        self.y_move *= -1





