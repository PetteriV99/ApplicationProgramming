from flask import Flask

app = Flask(__name__)


@app.route("/")
def myName():
    return "Hello Petteri Vänttinen!"


if __name__ == "__main__":
    app.run()
