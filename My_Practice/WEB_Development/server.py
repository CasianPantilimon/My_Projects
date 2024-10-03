from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! HELLLLLasdasdOOOOOO'

@app.route('/blog')
def blog():
    return 'Welcome to the blog'


if __name__ == '__main__':
    app.run(debug=True)
