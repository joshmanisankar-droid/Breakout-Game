from turtle import *

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.goto(0,-400)
    def move_left(self):
        new_x=self.xcor()-20
        if new_x>-450:
            self.goto(new_x,self.ycor())
    def move_right(self):
        new_x=self.xcor()+20
        if new_x<450:
            self.goto(new_x,self.ycor())
    