from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.punkty = 0
        self.penup()
        if side == "prawa":
            start_x = 250
        elif side == "lewa":
            start_x = -250 
        self.goto(start_x, 270)    
        self.color("white")
        self.ht()
        self.write(f'{self.punkty}', align= "center", font = ("Courier", 16 , "bold"))
       

    def nowy_punkt(self):
        self.punkty += 1
        self.clear()
        self.write(f'{self.punkty}', align= "center", font = ("Courier", 16 , "bold"))

