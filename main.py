from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=900)
screen.title("Breakout Game")
screen.tracer(0)

#initialize the paddle
paddle = Paddle()

screen.listen()
screen.onkey(key="Left",fun=paddle.go_left)
screen.onkey(key="Right",fun=paddle.go_right)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()