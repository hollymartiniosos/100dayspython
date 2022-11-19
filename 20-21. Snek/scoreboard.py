from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.punkty = 0
        self.high_score = self.highest_score_ever()
        
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.ht()
        
        
        self.write(f'Scoreboard: {self.punkty} High Score: {self.high_score}', align= "center", font = ("Courier", 16 , "bold"))
        
    def highest_score_ever(self):
        with open("data.txt", mode = "r") as file:
           loaded_score = int(file.read())
           
           
           return loaded_score

    def changing_highest_score(self):
        with open("data.txt", mode = "w") as file:
           file.write(str(self.high_score))
           
           
           
           
    def comparing_scores(self): 

        if self.punkty > self.high_score:
            self.high_score = self.punkty 
            self.changing_highest_score()
           
            
          

    def nowy_punkt(self):
        self.punkty += 1
        self.comparing_scores()
        self.update_scoreboard()

    def update_scoreboard(self):    
        self.clear()
        self.write(f'Scoreboard: {self.punkty}  High Score: {self.high_score}', align= "center", font = ("Courier", 16 , "bold"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER', align= "center", font = ("Courier", 16 , "bold"))    

    def reset(self) -> None:
        if self.punkty > self.high_score:
            self.high_score = self.punkty
        self.punkty = 0 
        self.update_scoreboard()    