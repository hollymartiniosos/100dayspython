from secrets import choice
from turtle  import Turtle, Screen, colormode, onclick
import turtle as t
import random

tio =Turtle()

tio.shape("turtle")
t.colormode(255)
tio.color(40,80,120)
"""Challenge 1 - turtle doing squere"""
# tio.forward(100)
# tio.right(90)
# tio.forward(100)
# tio.right(90)
# tio.forward(100)
# tio.right(90)
# tio.forward(100)

"""Challenge 2 - dash line"""

# for _ in range(15):
#     tio.pd()
#     tio.fd(10)
#     tio.pu()
#     tio.fd(10)

"""Challenge 3 = płacz i zgrzytanie zębami"""

# for n in range(3,11):
#     tio.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     for _ in range(n):
#         tio.fd(100)
#         tio.right(180 -((180*(1+(n-3)))/n))



"""Challenge 4  - random walk"""
# screen = Screen()
# screen.exitonclick()
# walk = [0, 90, 180, 270]
# z = True



# while True:
#     tio.pensize(20)
#     tio.pen(speed = 5)
#     tio.turtlesize(2, 2 , 2)
#     tio.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#     tio.right(random.choice(walk))
#     tio.fd(100)
   

"""Challenge 5 - wzory z kółek"""



def draw_spirograph(angle):
    for _ in range(360//angle):
        tio.pensize(2)
        tio.pen(speed = 0)
        tio.turtlesize(2, 2 , 2)
        tio.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        tio.circle(50)
        tio.left(angle)
    
draw_spirograph(10)




screen = Screen()
screen.exitonclick()