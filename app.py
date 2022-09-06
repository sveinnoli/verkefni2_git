from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Prentar hello world á root"""
    return "Hello, World!"

@app.route("/blog")
def blog():
    return "blog"

@app.route("/test")
def test():
    return "test"