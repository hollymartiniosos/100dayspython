import turtle

class Paletka(turtle.Turtle):
    
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.penup()
        if side == "prawa":
            start_x = 350
        elif side == "lewa":
            start_x = -350 
        else: 
            print("Nie działa")  

        self.goto(x = start_x, y = 0)
        self.setheading(90)
        self.shapesize(stretch_len = 5)
        self.color("white")

    def up(self):
        if self.ycor() < 260:
            self.forward(20)

    def down(self):
        if self.ycor() > -260:
            self.back(20)  