from turtle import Turtle,Screen

tur=Turtle()
screen=Screen()

def move_forwards():
    tur.forward(10)
    
def move_backwards():
    tur.backward(10)
    
def turn_left():
    new_heading=tur.heading()+10
    tur.setheading(new_heading)
    
def turn_right():
    new_heading=tur.heading()-10
    tur.setheading(new_heading)

def clear():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()