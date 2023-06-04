from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe location on Google Maps (URL)', validators=[DataRequired() ])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 2PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffe Rating', validators=[DataRequired()] , choices=(['✘'] + ["☕️" * i for i in range(1,6)]))
    wifi = SelectField('WiFi Strength Rating', validators=[DataRequired()], choices=(['✘']+["💪" * i for i in range(1,6)]))
    power = SelectField('Power Socket Availability', validators=[DataRequired()], choices=(['✘'] + ["🔌" * i for i in range(1,6)]))

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
def main():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = list(form.data.values())[:7]
        with open('cafe-data.csv',"a", newline='', encoding='utf-8') as csv_file:
            new_row_writer = csv.writer(csv_file, delimiter=',')
            new_row_writer.writerow(new_row)
   
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
          
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
