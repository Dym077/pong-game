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

# TODO 5: Make the ball move
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)






