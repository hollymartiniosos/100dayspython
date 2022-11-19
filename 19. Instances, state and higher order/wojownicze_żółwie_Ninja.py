from turtle import Turtle, Screen, forward
import random
is_race_on = False
"""Screen set up - width, height"""
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt="Który żółw Ninja jest najszybszy? Podaj imię: ")

print(user_bet)

Leonardo = Turtle()
Leonardo.shape("turtle")
Leonardo.color("deep sky blue")
Leonardo.penup()
Leonardo.setposition(-230, -150)


Donatello  = Turtle()
Donatello.shape("turtle")
Donatello.color("dark orchid")
Donatello.penup()
Donatello.setposition(-230, -50)

Michelangelo  = Turtle()
Michelangelo.shape("turtle")
Michelangelo.color("orange")  
Michelangelo.penup()      
Michelangelo.setposition(-230, 50)

Raphael = Turtle()
Raphael.shape("turtle")
Raphael.color("red")
Raphael.penup()
Raphael.setposition(-230, 150)

imiona = ["Leonardo", "Donatello", "Michelangelo", "Raphael"]
żółwie = [Leonardo, Donatello, Michelangelo, Raphael]

if user_bet:
   is_race_on = True 

while is_race_on:
    for żółw in żółwie:
        żółw.forward(random.randint(0,10))
    for i, żółw in enumerate(żółwie):
        if żółw.xcor() > 250:
            is_race_on = False
            wygryw = imiona[i]   

if wygryw == user_bet:
    print(f'You won! {wygryw} is the best!')        
else:
    print(f'You lose. {wygryw} has beaten {user_bet} this time!')        

screen.exitonclick()