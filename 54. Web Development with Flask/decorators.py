import time

def decorator_function(function):
    def wrapper_function():
        #DO SOMETHING BEFORE FUNCTION
        #MODIFY FUNCTION ex. run it twice
        function()
        #DO SOMETHING AFTER FUNCTION
    return wrapper_function


def delay_decorator(function):
    def wrapper_function():
        print("waiting")
        time.sleep(3)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello") 


say_hello()

# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {args}")
    return wrapper    

# Use the decorator 👇
@logging_decorator
def a_func(a, b, c):
    return a*b*c


a_func(1,2,3)