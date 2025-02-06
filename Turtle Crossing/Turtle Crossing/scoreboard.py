from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT2= ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        with open("data.txt") as file:
            self.high_score=file.read()
        self.hideturtle()
        self.penup()
        self.teleport(-280,260)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}   HIGH: {self.high_score}",align="left",font=FONT)
        

    def increase_level(self): 
        self.level+=1
        
        
        if self.level>int(self.high_score):
            self.high_score=self.level
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
                

        self.update_scoreboard()
        
    def game_over(self):
        self.teleport(0,0)
        self.write("GAME OVER",align="center",font=FONT2)