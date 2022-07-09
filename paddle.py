from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.color("white")

    def move_right(self):
        x = self.xcor() + 20
        y = self.ycor()
        if self.xcor() < 320:
            self.goto(x,y)

    def move_left(self):
        x = self.xcor() - 20
        y = self.ycor()
        if self.xcor() > -330:
            self.goto(x,y)