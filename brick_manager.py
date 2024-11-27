
from turtle import Turtle

COLORS = ["red", "orange", "yellow","green"]

class BrickManager:

    def __init__(self):
        self.all_bricks = []

    def create_bricks(self):
        #brick starting position
        x,y= -350,100
        #lay the bricks
        for i in range(len(COLORS)):
            while x < 380:
                new_brick = Turtle("square")
                new_brick.color(COLORS[i])
                new_brick.penup()
                new_brick.shapesize(stretch_len=3, stretch_wid=2)
                new_brick.goto(x, y)
                self.all_bricks.append(new_brick)
                x += 70
            x= -350
            y += 50

    def detect_collision(self,ball):

        for brick in self.all_bricks:
            #check ball coordinates and brick coordinates for collision
            if ball.distance(brick) < 50 and brick.xcor()-50 <= ball.xcor() <= brick.xcor()+50 and brick.ycor() - 50 <= ball.ycor() <= brick.ycor()+50:
                #delete the turtle from screen
                brick.reset()
                return True
