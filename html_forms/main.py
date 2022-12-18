from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    # request.form taps into the info entered by the user on the form. Needs to have matching name attribute
    message = f"Name: {request.form['name']}, Password: {request.form['password']}"
    return f"<h1>{message}</h1>"

if __name__ == "__main__":
    app.run(debug=True)