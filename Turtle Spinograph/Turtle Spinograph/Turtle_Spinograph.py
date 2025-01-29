from turtle import Turtle
import turtle
import random

turtle.colormode(255)
turt=Turtle()
turt.pensize(2)
turt.speed("fastest")


for i in range(0,360,3):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turt.color(r,g,b)
    turt.circle(100)
    turt.penup()             #baktýðý yeri heading() ile deðiþtirebiliriz de 
    turt.right(i)
    turt.pendown()
