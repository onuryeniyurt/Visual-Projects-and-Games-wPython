from turtle import Turtle,Screen
import random
race_on=False

screen=Screen()
screen.setup(width=500,height=400)
user_guess= user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")

colors=["purple","red","blue","orange","green","yellow"]
all_turtles=[]

for x in range(0,6):
    
    turtle_=Turtle(shape="turtle")
    turtle_.penup()
    turtle_.color(colors[x])
    turtle_.goto(x=-230,y=-130 + x*40)
    all_turtles.append(turtle_)
    
if user_guess:
    race_on=True
    
while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            if winning_color==user_guess:
                print(f"You win! The winning color is {winning_color}")
                race_on=False
            else:
                print(f"You lose! The winning color is {winning_color}")
                race_on=False

        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)
        
    
    
