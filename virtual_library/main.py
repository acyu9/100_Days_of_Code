from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up SQLAlchemy
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Set up database structure
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f'<Books {self.title}>'


# Create database
db.create_all()


# Homepage displays books from database
@app.route('/', methods=["GET", "POST"])
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)


# Add function to add new book to database
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form.get("name"),
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template("add.html")


# Edit function to change specific book's rating
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        selected_book = Book.query.get(id)
        selected_book.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for("home"))

    selected_book = Book.query.get(id)
    return render_template("edit.html", book=selected_book)


# Delete function to remove specific book from homepage & database
@app.route("/delete/<id>")
def delete(id):
    selected_book = Book.query.get(id)
    db.session.delete(selected_book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

