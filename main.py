import time
from turtle import Turtle, Screen
from paddle import Paddle
from brick_manager import BrickManager
from ball import Ball

FONT = ("Courier", 30, "normal")
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=900)
screen.title("Breakout Game")
screen.tracer(0)

#initialize the paddle
paddle = Paddle()
brick = BrickManager()
brick.create_bricks()
ball = Ball()
screen.listen()
screen.onkey(key="Left",fun=paddle.go_left)
screen.onkey(key="Right",fun=paddle.go_right)

game_is_on = True
while game_is_on:
    #smooth out the ball movement
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with side wall.
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    # Detect collision with top wall.
    if ball.ycor() > 430:
        ball.bounce_y()
    # Detect collision with brick and ball
    if brick.detect_collision(ball):
        #after deleting the brick after collision update the screen
        screen.update()
        #bounce the ball
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -380:
        ball.bounce_y()
    #Detect missed to catch the ball
    if ball.ycor() < -500:
        game_is_on = False
        #Write Game over on screen
        game_over = Turtle()
        game_over.color("white")
        game_over.penup()
        game_over.goto(0, 0)
        game_over.write(f"GAME OVER", align="center", font=FONT)

screen.exitonclick()