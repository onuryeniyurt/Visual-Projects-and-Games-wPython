import turtle
from turtle import Turtle
import random

directions=[0,90,180,270]

turtle.colormode(255)   #bunu yazmadan rgb deðeri veremiyoz renklere

turt=Turtle()
turt.pensize(15)
turt.speed(5)


for i in range(100):
    b=random.randint(0,255)
    g=random.randint(0,255)
    r=random.randint(0,255)
    turt.pencolor(b,g,r)
    s=random.randint(0,100)
    turt.forward(s)
    turt.right(random.choice(directions))