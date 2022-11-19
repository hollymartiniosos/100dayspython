from turtle import Turtle
import random
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

def create_car(x):
    car = Turtle()
    car.shape("square")
    car.penup()
    car.shapesize(stretch_len = 3)
    car.color(random.choice(COLORS))
    car.setheading(180)
    y = random.randint(-25, 25)*10
    car.goto(x, y)
    return car

class CarManager:
    def __init__(self) -> None:
        self.speed = STARTING_MOVE_DISTANCE
        
        self.cars = []
        for _ in range(15):
            car = create_car(random.randint(-300, 300))
            self.cars.append(car)


    def move(self):
        for car in self.cars:
            car.forward(self.speed)
       

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def czyszczenie(self):
        new_cars = []
        for i in range(len(self.cars)):
            if  self.cars[i].xcor() < -300:
                self.cars[i].ht()
                self.cars[i] = 0
                
            else:
                new_cars.append(self.cars[i])

        self.cars = new_cars   

    def nowe_auta(self):
        if len(self.cars) < 15:
            for _ in range(random.randint(1,3)):
                self.cars.append(create_car(300))


                




