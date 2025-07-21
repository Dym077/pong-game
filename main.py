from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

ball = Ball()
# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    ball.move()
    screen.update()

screen.exitonclick()



