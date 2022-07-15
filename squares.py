#squares.py
from turtle import Turtle

class Square(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=2)
        self.color("blue")

    