from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Introduction to CI & CD | Baysan"


@app.route("/greeting/<name>")
def greeting(name):
    return f"Hello, {name}!"

@app.route('/medium/')
def medium():
    return 'I am testing the CD for medium.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
