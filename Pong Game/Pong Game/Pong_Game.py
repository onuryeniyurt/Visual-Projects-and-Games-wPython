from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

paddle_r=Paddle((350,0))
paddle_l=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(paddle_r.go_up,"Up")
screen.onkeypress(paddle_r.go_down,"Down")
screen.onkeypress(paddle_l.go_up,"w")
screen.onkeypress(paddle_l.go_down,"s")

game_on=True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        
    if ball.distance(paddle_r)<41 and ball.xcor()>320 or ball.distance(paddle_l)<41 and ball.xcor()<-320:
        
        ball.bounce_x()
        
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.l_point()
        
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.r_point()
        


screen.exitonclick()

