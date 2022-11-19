import colorgram

from turtle  import Turtle, Screen, colormode, onclick
import turtle as t
import random
t.colormode(255) 
tio =Turtle()
tio.hideturtle()
colors = colorgram.extract("obraz.jpg", 30)
rgb_colors = []
for item in colors:
   rgb = tuple(item.rgb) 
   rgb_colors.append(rgb)

print(rgb_colors)

# Jasia popis <3
# rgb_colors = [tuple(color.rgb) for color in colorgram.extract("obraz.jpg", 30)]

# color_list = [(212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65)]

color_list = rgb_colors[2:] 
tio.penup()
tio.setposition(-225, -225)

for item in range(0, 10):
    for _ in range(0, 10):
        tio.color(random.choice(color_list))
        tio.dot(10)
        tio.fd(50)
    new_pos = (-225, 50 * (item + 1) - 225)
    tio.setposition(new_pos)
       

screen = Screen()
screen.exitonclick()