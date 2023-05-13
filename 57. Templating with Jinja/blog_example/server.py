from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('indexm.html')

@app.route('/blog/<num>')
def get_blog(num):
    #getting blog details from https://www.npoint.io/ - fake blog
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template('blog.html', posts = data)


if __name__=="__main__":
    app.run(debug=True)