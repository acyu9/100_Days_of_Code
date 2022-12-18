from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<blog_id>")
def get_blog(blog_id):
    requested_post = None
    for post in all_posts:
        if post["id"] == int(blog_id):
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
