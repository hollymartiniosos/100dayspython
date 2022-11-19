import turtle

#calling template(class) from turtle module
#turtle - module
#Turtle - class, without brackets. Brackets are added when calling to create an object.

timmy = turtle.Turtle()

#Creating/Printing/Calling Objects Attributes - jak się dostać do tego co jest w timmy
#To check what is in the called thing   ctrl + click



timmy.shape("turtle")
timmy.color("BlueViolet")

#to check what attributes and methods object has
print(dir(timmy))

my_screen = turtle.Screen()
timmy.forward(100)
timmy.turtlesize(20,15,20)
my_screen.exitonclick()