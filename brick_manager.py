import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [()]

class BrickManager:

    def __init__(self):
        self.all_bricks = []

    def create_bricks(self):

        new_brick = Turtle("square")
        new_brick.color(random.choice(COLORS))
        new_brick.penup()
        new_brick.shapesize(stretch_len=3, stretch_wid=2)
        random_y = random.randint(-250, 250)
        new_brick.goto(300, random_y)
        self.all_bricks.append(new_brick)

