from tkinter import *

#the class creating the window
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width= 300, height= 200)
window.config(padx=20, pady=20)


is_equal_to = Label(text = "is equal to", font=("Arial" , 15 ))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=20, pady=20)

miles = Label(text = "Miles", font=("Arial" , 15 ))
miles.grid(column=2, row=0)
miles.config(padx=20, pady=20)

km = Label(text = "Kilometers", font=("Arial" , 15 ))
km.grid(column=2, row=1)
km.config(padx=20, pady=20)

km_calc = Label(text = "0" , font=("Arial" , 15 ))
km_calc.grid(column=1, row=1)
km_calc.config(padx=20, pady=20)

#Creating Button
def button_clicked():
    
    m = float(input.get())
    km_calc.config(text = round(m*1.609, 2))

button = Button(text = "Calculate", command= button_clicked)
button.grid(column=1, row=2)




# Entry / Input field

input= Entry(width= 10)
input.grid(column=1, row=0)



# this function will keep window open on the screen and listen for any further action the user may want to do
window.mainloop()