from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Introduction to CI & CD | Baysan"


@app.route("/greeting/<name>")
def greeting(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
