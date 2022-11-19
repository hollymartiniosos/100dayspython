from turtle import Turtle
import random
class Piłka(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.szybkosc = 20
        self.znak_y = random.choice([-1,1])
        self.znak_x = random.choice([-1,1])
        self.reset()
        print(self.kierunek_x, self.kierunek_y)

    """Piłka się rusza w while loop w main (za każdym razem gdy funkcja jest wywałana w pętli zmienia się pozycja piłki) 
    a poniższa funkcja wywołuje tylko przesunięcie piłki o określoną wartość jako dx lub dy"""

    def move(self):
        x_0 = self.xcor()
        y_0 = self.ycor()
        dx = self.kierunek_x * self.szybkosc * self.znak_x
        dy = self.kierunek_y * self.szybkosc * self.znak_y
        x_1 = x_0+dx
        y_1 = y_0+dy
        self.goto(x= x_1, y= y_1)

    def wall_bounce(self):
        self.znak_y *= -1

    def paletka_bounce(self):
        self.znak_x *= -1

    def reset(self):
        self.goto(0,0)
        self.kierunek_x = random.randint(1,50)
        self.kierunek_y = random.randint(1,50)
        dlugosc = (self.kierunek_x **2 + self.kierunek_y **2)**0.5
        self.kierunek_x /= dlugosc
        self.kierunek_y /= dlugosc
        self.znak_x *= -1
