from art import logo 
from art import vs
import random
import game_data

print(logo)

def choices_AB():
    Compare_A = random.choice(list(game_data.data))
    print(f'Compare A: {Compare_A["name"]}, a {Compare_A["description"]}, from {Compare_A["country"]}.') 

    print(vs)

    Against_B = random.choice(list(game_data.data)) 
    while Against_B == Compare_A:
        Against_B = random.choice(list(game_data.data)) 

    print(f'Against B: {Against_B["name"]}, a {Against_B["description"]}, from {Against_B["country"]}.') 
    return Compare_A, Against_B

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
    A, B = choices_AB()
    print(f'pierwsze {A} i pierwsze {B}')

    G = user_guess(A,B)
    print(f'pierwszy guess {G}')
   
    C = comparison(A,B)   
    print(f'piersze sprawdzenie {C}')    

    EG = check_if_correct(G, C)
    

    while EG == False:
        score += 1
        print(f'You are right! Current score: {score}.')
        A = B
        print(f'Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.') 
        print(vs)
        B = random.choice(game_data.data)
        while B == A:
            B = random.choice(game_data.data)  
        print(f'Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.') 
        G = user_guess(A, B)
        C = comparison(A, B)
        EG = check_if_correct(G, C)
         
        

    print(f"Sorry, that's wrong. Final score: {score}")

game()
