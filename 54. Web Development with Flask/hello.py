from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>'\
#             '<p>Cute little Kitten</p>' \
#             '<img src="https://i.pinimg.com/originals/99/da/b9/99dab9d31ffc8b3b631d73f73005cd89.gif" width=200>'

# if __name__=="__main__":
#     app.run()


# w nawiasach ostrych podaje sie zmienna do flaska <name> - w przeglądarce mozna wpisac swoje imie za / i pokaze je na stronie

# @app.route('/<name>')
# def hello_world(name):
#     return f'Hello, {name}!'

def make_bold_decorator(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underscore(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function


@app.route('/')
@make_bold_decorator
@make_emphasis
@make_underscore
def bye():
    return "Bye!"

bye()   


if __name__=="__main__":
    app.run(debug=True)
