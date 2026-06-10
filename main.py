from turtle import *
from player import Player
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard

screen=Screen()
screen.setup(1000,1000)
screen.bgcolor("black")
screen.title("Break Out")
screen.tracer(0)
screen.listen()
player=Player()
ball=Ball()
scoreboard=Scoreboard()

bricks=[]
colors=["red","green","orange","yellow","blue"]
for row in range(5):
    for col in range(10):

        x=-360+col*80
        y=400-row*40
        brick = Brick(x, y, colors[row])
        bricks.append(brick)


game_is_on=True
while game_is_on:
    
    screen.update()

    screen.onkeypress(player.move_left,"Left")
    screen.onkeypress(player.move_right,"Right")
    ball.move()
    for brick in bricks[:]:
        if ball.distance(brick)<35:
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.increse_score()
            ball.bounce_y()
            break
    if ball.xcor()>490 or ball.xcor()<-490:
        ball.bounce_x()

    if ball.ycor()>490:
        ball.bounce_y()

    if ball.distance(player)<60 and ball.ycor()<-380:
        ball.bounce_y()

    if ball.ycor()<-500:
        scoreboard.lost()
        game_is_on=False

    if len(bricks)==0:
        scoreboard.won()
        game_is_on=False

screen.mainloop()