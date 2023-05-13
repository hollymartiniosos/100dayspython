from flask import Flask, render_template
import requests


response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
all_posts = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def my_posts(num):
    current_post = None
    for post in all_posts:
        if post['id'] == num:
            current_post = post
    return render_template('post.html', post=current_post)


if __name__ == "__main__":
    app.run(debug=True)