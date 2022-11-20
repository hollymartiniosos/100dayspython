from tkinter import *

#the class creating the window
window = Tk()
window.title("My first GPU")
window.minsize(width= 500, height= 300)
# creating space between objects
window.config(padx=20, pady=20)


#Creating lebel, but it no show on the window before it's packed; Label is a class so has to be capitol letter L
my_label = Label(text = "I am a label", font=("Arial" , 24 , "bold"))
# my_label.place(x=100, y=100)

#config can change existing text
my_label["text"] = "New Text"
my_label.config(text = "New Text")
#Pack will lay the label (or any component) on the screen
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

#Creating Button
def button_clicked():
    
    m = input.get()
    my_label.config(text = m)

button = Button(text = "Click me", command= button_clicked)
button.grid(column=1, row=1)

new_button = Button(text = "New one")
new_button.grid(column=2, row=0)


# Entry / Input field

input= Entry(width= 10)
input.grid(column=3, row=2)



# this function will keep window open on the screen and listen for any further action the user may want to do
window.mainloop()

#pack() will always start from the top in the center - can define the side; it's difficult to specify exact position
#place() specify where to lay out the component by x, y coor; 0,0 is in the left top corner
#grid() change the whole window to the grid, you can define number of rows and columns; 
# can't mix grid() and pack() methods; grid() is favorable in terms of how to use it and place items;
