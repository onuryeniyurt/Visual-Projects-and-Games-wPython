import colorgram
import turtle
import random
from turtle import Turtle
colors=colorgram.extract('resim.jpg',30)

rgb_colors=[]

for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
    
print(rgb_colors)

turtle.colormode(255)

turt=Turtle()
turt.speed("fastest")
turt.penup()
turt.hideturtle()

turt.setheading(225)
turt.forward(300)
turt.setheading(0)

num_of_dots=100

for i in range(1,num_of_dots+1):

    turt.dot(20,random.choice(rgb_colors))
    turt.forward(50)
    if i%10==0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)

screen=turtle.Screen()
screen.exitonclick()

