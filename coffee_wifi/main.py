from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, url
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# Create form via WTForms for user to fill out
class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = URLField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), url()])
    opening = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    closing = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField(label='Coffee Rating', 
        choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
        validators=[DataRequired()])
    wifi = SelectField(label='Wifi Strength Rating', 
        choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
        validators=[DataRequired()])
    power = SelectField(label='Power Socket Availability',
        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
        validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    # POST
    if form.validate_on_submit():
        # Create & clean the list of data entered by user
        new_cafe = []
        for ele in form:
            new_cafe.append(ele.data)
        new_cafe = new_cafe[:-2]

        # Update the csv file with new cafe data
        with open('cafe-data.csv', mode='a', encoding="utf8") as csv_file:
            new_cafe_string = ','.join(new_cafe)
            csv_file.write('\n' + new_cafe_string)
        return redirect(url_for('cafes'))
    
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
