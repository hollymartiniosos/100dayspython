import time
from turtle import Screen
from player import Player 
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)
screen.bgcolor("White")
screen.title("Turtle Crossing")

player = Player()
scoreboard = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.czyszczenie()
    cars.nowe_auta()

    if player.ycor() == 280:
        scoreboard.level_up()
        cars.speed_up()
        player.reset() 

    for car in cars.cars:
        
        if abs(car.xcor() - player.xcor()) < 40 and abs(car.ycor() - player.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()  

            
        






screen.exitonclick()