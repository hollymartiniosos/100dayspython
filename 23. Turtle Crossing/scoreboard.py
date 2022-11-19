FONT = ('Courier', 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-200, 270)    
        self.color("black")
        self.ht()
        self.write(f'Level: {self.level}', align= "center", font = ("Courier", 20 , "bold"))
       

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align= "center", font = ("Courier", 20 , "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align= "center", font = ("Courier", 24 , "bold"))  