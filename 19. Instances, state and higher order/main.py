from turtle import Turtle, Screen

tio = Turtle()
screen = Screen()
tio.shape("turtle")
tio.color("blueviolet")

"""Move Forward when 'w' is clicked"""
def w():
    tio.fd(10)

"""Move Backwards when 's' is clicked"""
def s():
    tio.bk(10)
    
"""Rotate Counter-Clockwise when 'a' is clicked"""
def a():
    tio.lt(10)

"""Rotate Clockwise when 'd' is clicked"""
def d():
    tio.rt(10) 

"""Clear drawing when 'c' is clicked"""
def c():
   tio.reset()

        

screen.onkeypress(w, "w")
screen.onkeypress(s, "s")
screen.onkeypress(a, "a")
screen.onkeypress(d, "d")
screen.onkeypress(c, "c")


screen.listen()
screen.exitonclick()