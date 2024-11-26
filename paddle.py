from turtle import Turtle
class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=6)
        self.color("white")
        self.setheading(0)
        self.goto((0,-400))
        print("initialize paddle")

    def go_left(self):
        self.backward(20)

    def go_right(self):
        self.forward(20)

