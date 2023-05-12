from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home(name=None):
    return render_template('index.html', name = name)
#index.html have to be in the folder called templates, otherwise flask won't find it

if __name__=="__main__":
    app.run(debug=True)