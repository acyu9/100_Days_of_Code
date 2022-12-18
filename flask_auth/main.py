from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
# A Mixin is a way to provide multiple inheritance. This one includes flask-login methods
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


# Going to a page that acccesses current_user requires Flask-Login to create a User object from the 
# stored user_id. This is done by calling the user_loader decorator, though it's not explicitly called
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method=="POST":
        # User already exists
        if User.query.filter_by(email=request.form.get("email")).first():
            flash("You've already signed up wtih that email. Please log in.")
            return redirect(url_for("login"))

        # Create hashed and salted password
        secure_password = generate_password_hash(
        password=request.form.get("password"), 
        method="pbkdf2:sha256", 
        salt_length=8
        )
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=secure_password
        )
        db.session.add(new_user)
        # If getting an error for commit(), check the instance folder, that it has the correct db file
        # If manually editing DB Browser, save before trying the code
        db.session.commit()

        # Log in and authenticate user after adding to database
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")

        # Find user by email; email is unique
        user = User.query.filter_by(email=email).first()

        # If email doesn't exist
        if not user:
            flash("The email entered doesn't exist in the database.")
            return redirect(url_for("login"))

        # Check stored password hash against entered password
        elif not check_password_hash(pwhash=user.password, password=password):
            flash("The password is incorrect.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("secrets"))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
# Decorator that require user to be logged in to view the page
@login_required
def secrets(): 
    # Access the logged-in user with current_user
        return render_template("secrets.html", name=current_user.name, log_in=True)


@app.route('/logout')
def logout():
    pass


@app.route('/download/')
@login_required
def download():
    return send_from_directory(directory="static/files", path="cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
