from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home(name=None):
    random_number = random.randint(0,10)
    year_now = datetime.now().year
    return render_template('index.html', name = name, num=random_number, year = year_now )


if __name__=="__main__":
    app.run(debug=True)