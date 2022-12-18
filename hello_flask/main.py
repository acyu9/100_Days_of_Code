# For this to work, use command prompt in terminal. Follow documentation (include set in command)
# set FLASK_APP=main.py then flask run
# To turn on debugger, set debug=True AND type in command prompt
# set FLASK_ENV=development then flask run
# Debugger PIN in terminal can be used to live debug the website

from flask import Flask

app = Flask(__name__)

def make_bold(function):
    # *args = positional argument, **kwargs = keyword argument
    def wrapper(*args, **kwargs):
        # These parameters can call any function with any combo of args and kwargs
        return "<b>" + function(*args, **kwargs) + "</b>"
        # function(args[0]) gives tuple index out of range error.
        # function(*args) gives missing 2 required positional arguments Type Error
        # The @app.route('/<name>') calls greet() with keyword args so **kwargs needed in function
        # Without @app.route(), it's positional argument --- see advanced_decorator.py
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello, World!' \
        '<img src="https://media.giphy.com/media/X3Yj4XXXieKYM/giphy.gif">'

@app.route('/<name>/<number>')
@make_bold
def greet(name, number):
    return f"Good morning, {name}. You are {number} years old."


if __name__ == "__main__":
    # No need to reload the website every time; updates with save automatically
    app.run(debug=True)