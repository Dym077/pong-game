from turtle import Turtle
import random as r

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0.0)
        self.color("white")
        self.pu()
        self.shape("circle")
        self.goto(0,0)
        self.rand_pos()

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def rand_pos(self):
        directions = [-1, 1]
        self.x_move = 2.5 * r.choice(directions)
        self.y_move = 2.5 * r.choice(directions)




