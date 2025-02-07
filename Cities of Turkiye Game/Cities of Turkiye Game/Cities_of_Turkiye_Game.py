from turtle import Turtle,Screen
import pandas as pd

screen=Screen()
screen.title("Cities of Turkey Game")
screen.setup(1400,720)

path="turkiye.gif"

screen.addshape(path)

map_1=Turtle()

corrects=0


map_1.shape(path)

# def get_mouse_click_coor(x,y):
#     print(x,y)
    

# screen.onscreenclick(get_mouse_click_coor)

# screen.mainloop()

dataset = pd.read_csv("cities_of_turkey.csv")

guesses=[]


game_on=True

while game_on:
    answer=screen.textinput(title=f"{corrects}/81 Cities of Turkiye",prompt="City in Turkiye:")
    for xx in dataset["cities"]:
        if answer in guesses:
            pass
        elif answer==xx.lower():
            pin=Turtle()           
            pin.penup()           
            pin.hideturtle()
            pin.speed("fastest")
            new_data=dataset[dataset.cities==answer.capitalize()]
            pin.goto(int(new_data.x),int(new_data.y))
            pin.write(xx,align="center", font=("Arial", 12, "bold"))
            guesses.append(answer)
            corrects+=1
            
    if corrects==81:
        screen.clear()
        turt=Turtle()
        turt.penup()
        turt.hideturtle()
        turt.write("WELL DONE! You found all of the cities of Turkiye!", align="center", font=("Arial", 24, "bold"))
        game_on=False
            
            





screen.exitonclick()
