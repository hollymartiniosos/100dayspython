from art import logo 
from art import vs
import random
import game_data
# import os

print(logo)

def choose_B(A):
    
    Against_B = random.choice(game_data.data) 
    while Against_B == A:
        Against_B = random.choice(game_data.data) 

     
    return Against_B

def user_guess(Compare_A, Against_B):
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == 'a':
        guess == Compare_A
        # print(guess)
    else:
        guess == Against_B
        # print(guess)
    
    return guess  

def comparison(Compare_A, Against_B):
    if int(Compare_A["follower_count"]) > int(Against_B["follower_count"]):
        correct_answer = 'a'
    else:
        correct_answer = 'b'
    # print (correct_answer)    
    return correct_answer

def check_if_correct(guess, correct_answer):
    if guess == correct_answer:
        end_game = False
    else:
        end_game = True   
    return  end_game      


def game():
    score = 0
    EG = False
    A = random.choice(game_data.data)
    

      

    while EG == False:
        #os.system('cls')
        
        print(f'Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.') 
        B = choose_B(A)
        print(vs)
        print(f'Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.') 
        
        G = user_guess(A, B)
        C = comparison(A, B)
        EG = check_if_correct(G, C)
        if not EG:
            A = B
            score +=1
            print(f'You are right! Current score: {score}.')
        

    print(f"Sorry, that's wrong. Final score: {score}")

game()
