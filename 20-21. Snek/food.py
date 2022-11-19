from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()   
        self.shape("circle") 
        self.penup()
        self.shapesize(0.5 , 0.5)
        self.color("blue")
        self.speed("fastest")
        self.nowe_amciu()

    def nowe_amciu(self):    
        random_x = random.randint(-13, 13) *20
        random_y = random.randint(-13, 13) *20
        self.goto(random_x, random_y)