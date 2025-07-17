from turtle import Screen
from paddle import Paddle


# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.paddle_up,"Up")
screen.onkey(paddle.paddle_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()



