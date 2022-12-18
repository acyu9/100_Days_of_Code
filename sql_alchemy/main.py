from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy can help spot typos and errors

app = Flask(__name__)
app.app_context().push()

# Create database. USE ///, not 4 /'s, or will get OperationalError
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# Silence teh deprecation warning in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f'<Books {self.title}>'

# Create initial database
#with app.app_context():
#db.create_all()

# Add data to database
new_book = Book(title="Harry Potter 3", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

# Read all records
all_books = Book.query.all()

# Read particular record
book = Book.query.filter_by(title="Harry Potter").first()

# Update particular record by title
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

# Update particular record by primary key
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()

# Delete a particular record by primary key
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()