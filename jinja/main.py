from flask import Flask, render_template
from random import randint
from datetime import date
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    random_number = randint(1, 10)
    year = date.today().year
    # Can add as many **kwargs in render_template as needed
    return render_template("index.html", num=random_number, year=year, name="Annie")


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status()
    age = response.json()["age"]
    name = str(name).title()
    response2 = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = response2.json()["gender"]
    # Can also use jinja and a guess.html template
    return f"<h1>Hello {name},</h1> \
        <h2>I think you are {gender},</h2> \
        <h3>And maybe {age} years old.</h3>"


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)