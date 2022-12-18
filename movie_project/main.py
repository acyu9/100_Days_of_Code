from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Movie Database API Info
MOVIE_DB_SEARCH_URL = "some url here"
MOVIE_DB_API_KEY = "some key here"


# Set up SQLAlchemy
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

# Initializing the database
db.create_all()

# Add movie to database
# new_movie = Movie(
#     title = "Phone Booth",
#     year = 2002,
#     description = "Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating = 7.3,
#     ranking = 10,
#     review = "My favorite character was the caller.",
#     img_url = "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
# )
# db.session.add(new_movie)
# db.session.commit()

# Create edit form    
class EditForm(FlaskForm):
    # Label is what shows up on html. 
    rating = StringField(label="Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Update")


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")    

    
@app.route("/")
def home():
    # Sorts the movies by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # Reverse rating order
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    selected_movie = Movie.query.get(id)
    edit_form = EditForm()
    # Update the db; could also use edit_form.rating.data
    if edit_form.validate_on_submit():
        edit_form.populate_obj(selected_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=selected_movie, form=edit_form)


@app.route("/delete/<id>")
def delete(id):
    selected_movie = Movie.query.get(id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()

    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=add_form)


@app.route("/find")
def find():
    movie_api_id = request.args.get("id")
    if movie_api_id :
        movie_api_url = f"movie_db_info_url/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split(".")[0],
            img_url=f"movie_db_image_url{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit"))


if __name__ == '__main__':
    app.run(debug=True)
