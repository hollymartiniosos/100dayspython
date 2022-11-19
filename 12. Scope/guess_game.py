from art import logo
import random
print(logo)

zgadywana = random.randint(1, 100) 

print("I'm thinking of a number between 1 and 100.")
print(zgadywana)

diff_lvl = input("Choose a difficulty. Type 'easy' or 'hard':   ")

if diff_lvl == "easy":
    attempts = 10
else:
    attempts = 5

end_game = False 
while end_game == False: 

    print(f'You have {attempts} attempts remaining to guess the number.  ')  
    attempts -= 1 

    #zgadywanie przez użytkownika
    guess = int(input("Make a guess: "))

    if guess == zgadywana:
       end_game = True 
       print("You won! That's the number")
    elif guess < zgadywana:
        print("Too low.")
    else:
        print("Too high.") 

    if attempts == 0: 
        end_game = True
        print("You lose. Maybe try again.")




