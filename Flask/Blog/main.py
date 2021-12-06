from flask import Flask, render_template

app = Flask(__name__)

posts = [{
    'author': 'ii-ko',
    'title': 'programming',
    'content': 'Python programming',
    'date_posted': 'May 3rd, 2012'
},
{
    'author': 'tamae',
    'title': 'design',
    'content': 'Web design',
    'date_posted': 'May 4th, 2012'
},
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, port=3000)