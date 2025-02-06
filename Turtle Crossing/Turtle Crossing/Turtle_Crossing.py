import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if player.distance(car)<21:
            scoreboard.game_over()
            game_is_on=False
    
    if player.finish_line():
        player.teleport(0,-280)
        scoreboard.increase_level()
        car_manager.faster_cars()
        


screen.exitonclick()
