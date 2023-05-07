from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def higher_lower():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>'\
            '<img src="https://i.pinimg.com/originals/99/da/b9/99dab9d31ffc8b3b631d73f73005cd89.gif" width=200>'

number = random.randint(0,9)
print(number)

@app.route('/<int:guess>')
def user_guess(guess):
    if guess == number:
        return '<h1 style="text-align: center; color: red">You guessed it right!</h1>'\
                '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQViH637liHyEbjK1N4aLlVwDu_fX66bS_JmzQhy8lm&s" width=500>' 
    elif guess < number and 0<=guess:
        return '<h1 style="text-align: center; color: blue">That is too low!</h1>'\
                '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhowkwwexwaRjPNZzYBd5dA0c2yRghZti3QgN9uVs&s" width=500>'
    elif guess > number and guess<=9:
        return '<h1 style="text-align: center; color: green">That is too high!</h1>'\
                '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUMm1N9FExUQwgYVdUv4qIlLXAYwizxTU5wfU3oDg&s" width=500>'
    else:
        return '<h1 style="text-align: center">You are an idiot!</h1>'
    
     

if __name__=="__main__":
    app.run(debug=True)