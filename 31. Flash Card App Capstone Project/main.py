from tkinter import *
from tkinter import messagebox
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
# ------------------------ Picking a word ------------------------------#

def next_card():   
   global current_card, flip_timer 
   window.after_cancel(flip_timer)
   current_card = choice(to_learn)
   fr_word = current_card["French"]  
   canvas.itemconfig(card_title, text = "French", fill= "black")
   canvas.itemconfig(card_text, text = fr_word, fill="black")
   canvas.itemconfig(canvas_image, image= front_img)
   flip_timer = window.after(3000, flip_card)
#    words_to_learn = current_card.to_csv(index=False)
   
# -------------------- FLip the card ----------------------------------#
def flip_card():
    en_word = current_card["English"] 
    canvas.itemconfig(canvas_image, image= back_img)
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_text, text = en_word, fill="white")
  

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background= BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
canvas = Canvas(height=526, width=800, background= BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file = "images/card_front.png")
back_img = PhotoImage(file = "images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font= ("Ariel", 40, "italic"))
card_text = canvas.create_text(400,263, text="Word", font = ("Ariel", 60, "bold"))



right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, background= BACKGROUND_COLOR, command= is_known)
right_button.grid(row=1, column=1, columnspan=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong__button = Button(image=wrong_img, highlightthickness=0, background= BACKGROUND_COLOR, command= next_card)
wrong__button.grid(row=1, column=0, columnspan=1)



next_card()






window.mainloop()