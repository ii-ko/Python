from flask import Flask, render_template


app = Flask(__name__)

posts = [{
    'author': 'Ihsan',
    'title': 'First post',
    'content': 'First content',
    'date_posted': 'May 3rd, 2012'
    },
    {
        'author': 'Ahmad',
        'title': 'Second post',
        'content': 'Second content',
        'date_posted': 'May 3rd, 2012'
    }
]


@app.route('/')
def home():
    return render_template('pages/index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, port=3000)