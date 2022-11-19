from turtle import Screen
from paletka import Paletka
from piłka import Piłka
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paletka_1 = Paletka("prawa")
paletka_2 = Paletka("lewa")
ball = Piłka()
scoreboard_1 = Scoreboard("prawa")
scoreboard_2 = Scoreboard("lewa")

screen.listen()
screen.onkey(paletka_1.up, "Up")
screen.onkey(paletka_1.down, "Down")
screen.onkey(paletka_2.up, "w")
screen.onkey(paletka_2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #change direction if hit the wall
    #abs - wartość bezwzględna
    if abs(ball.ycor()) > 280:
        ball.wall_bounce()

    # change direction if hit the paddle(paletka)
    if ball.xcor() > 340:
        if abs(paletka_1.ycor() - ball.ycor()) <55:
            ball.paletka_bounce() 
        else:
            time.sleep(0.5)
            ball.reset()      
            scoreboard_2.nowy_punkt()

    if ball.xcor() < -340:
        if abs(paletka_2.ycor() - ball.ycor()) <55:
            ball.paletka_bounce()   
        else:
        # strata punktu
            time.sleep(0.5)
            ball.reset() 
            scoreboard_1.nowy_punkt()
    
    if scoreboard_1.punkty == 10 or scoreboard_2.punkty == 10:
        game_is_on = False
        


screen.exitonclick()