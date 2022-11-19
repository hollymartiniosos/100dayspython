import turtle
import pandas

screen =turtle.Screen()
screen.title("U.S. States Game")
image = "image.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_names = data.state.to_list()
#to get x and y value for each state
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


# ask the user for answer
game_is_on = True
score = 0
guess_list = []

# #check answer_state agains names of states from csv
while game_is_on:
    answer_state = screen.textinput(title= f"{score}/50 Guess the State", prompt = "What is another state's name?" ).title()
    if answer_state == "Exit": 
        states_to_learn = [ states for states in states_names if states not in guess_list]      
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False   

    if answer_state in states_names and answer_state not in guess_list:
        t = turtle.Turtle()
        t.ht()
        t.penup()
        row = data[data.state == answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(f'{answer_state}')
        score += 1
        guess_list.append(answer_state)
        if score == 50:
            game_is_on = False   
             
# states_to_learn.csv

#if yes, the name should be written on the map in correct place

#it continues even if it's wrong

#checking how many states has been already guessed out of 50 










#keeps the window open
turtle.mainloop()



