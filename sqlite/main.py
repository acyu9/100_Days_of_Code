import sqlite3

# Create connection to a new database (will be created if doesn't exist)
db = sqlite3.connect("book-collection.db")

# Create cursor to control database
cursor = db.cursor()


"""
- Actions in SQlite db are expressed as SQL (Structured Query Language) commands w/ keywords in ALL-CAPS
- CREATE TABLE called books
- () after create table are fields/column headings in the table
- First field is id with type INTEGER. Primary key = uniquely identify this column
- varchar(250) = variable-length string composed of char w/ max length of 250
- NOT NULL = can't be empty
- UNIQUE = no two records/headings in this table can have the same title
"""
# alt + z to auto-split long line into two
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Add data to table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()