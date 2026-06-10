from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

        self.color("white")
        self.penup()
        self.hideturtle
        self.goto(0,450)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"bold"))
    def increse_score(self):
        self.score+=1
        self.update_score()
    def win(self):
        self.goto(0,0)
        self.write("YOU WON!!!",align="center",font=("Arial",36,"bold"))
    def lost(self):
        self.goto(0,0)
        self.write("YOU LOST!!!",align="center",font=("Arial",36,"bold"))
    