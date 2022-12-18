from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

API_KEY = "TopSecretAPIKey"

##Connect to Database
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # Convert dict to json b/c similar structure & no need to type out all the data
    # Dict comprehension to set up dictionary of column name : column value (getattr)
    # Last part is tap into the Cafe db -> get the table -> get the columns -> get the column names
    def to_dict(self):
        dict_cafe = {column_name: getattr(self, column_name) for column_name in self.__table__.columns.keys()}
        return dict_cafe


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    # Pull up all cafes data then randomly choose one
    cafes = Cafe.query.all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()
    # There's more than 1 dict to put all dict in a list
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    # Returns the part in the URL after the ? in dict - loc: London
    query_location = request.args.get("loc")
    # Get all the cafes at that location
    matching_cafes = Cafe.query.filter_by(location=query_location).all()
    if matching_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in matching_cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    matching_cafe = Cafe.query.get(cafe_id)
    new_price = request.args.get("new_price")
    if matching_cafe:
        matching_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the coffee price."})
    return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    
    user_api = request.args.get("api-key")
    if user_api == API_KEY:
        matching_cafe = Cafe.query.get(cafe_id)
        if matching_cafe:
            db.session.delete(matching_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the closed cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key"}), 403

        
# Documentation should have the route and its function


if __name__ == '__main__':
    app.run(debug=True)
