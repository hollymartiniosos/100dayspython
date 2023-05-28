from flask import Flask, request, render_template
import requests

posts = requests.get('https://api.npoint.io/22fbfa78ef543e5a8ecf').json()


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("excercise.html")

@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f'<h1>Name: {name}  Password: {password}</h1>'

if __name__ == "__main__":
    app.run(debug=True)
