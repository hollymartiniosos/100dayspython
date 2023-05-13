from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Type your name</h1>'

@app.route('/guess/<name>')
def guess(name):
    hello = name.capitalize()
    #getting gender from genderize.io
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_data= gender_response.json()
    gender_guess = gender_data['gender']
    #getting age from agify.io
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age_data= age_response.json()
    age_guess = age_data['age']
     
    
    return render_template('index.html', name = hello, gender = gender_guess, age = age_guess  )


if __name__=="__main__":
    app.run(debug=True)