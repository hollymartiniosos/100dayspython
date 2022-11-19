from turtle import Screen
import time
from snek import Snek
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snek Game")
screen.tracer(0)

waz = Snek()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(waz.up, "Up")
screen.onkey(waz.down, "Down")
screen.onkey(waz.left, "Left")
screen.onkey(waz.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update() 
    waz.move()   
       
    #Detect collision with food. 
    if waz.segmenty[0].distance(food) <15:
        food.nowe_amciu()
        scoreboard.nowy_punkt()
        
        waz.extend()

    #Detect collision with wall.
    if waz.segmenty[0].xcor() > 280 or waz.segmenty[0].xcor() < -280 or waz.segmenty[0].ycor() > 280 or waz.segmenty[0].ycor() < -280:
       scoreboard.comparing_scores()
       scoreboard.reset()
       waz.reset_snek()    
       

    #Detect collision with tail.
    for s in waz.segmenty[1:]:
        if waz.segmenty[0].distance(s) < 10:
            scoreboard.comparing_scores()
            scoreboard.reset()    
            waz.reset_snek() 
            


screen.exitonclick()