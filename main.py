from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #print(f"Före studs: y={ball.ycor()}, y_move={ball.y_move}")
        ball.bounce_y()
        #print(f"Efter studs: y={ball.ycor()}, y_move={ball.y_move}")

    # TODO 7: Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO: Detect when paddle misses
    #Detect right paddle misses
    if ball.xcor() > 410:
        print("Ball is out of bounds")
        ball.reset_position()
        time.sleep(0.5)

        # Detect left paddle misses
    if ball.xcor() < -410:
        print("Ball is out of bounds")
        ball.reset_position()
        time.sleep(0.5)


screen.exitonclick()



