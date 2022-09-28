from flask import Flask

from appllication.services import create_table

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hi World!"


@app.route("/phone_book")
def phones():  # put application's code here
    return create_table()


if __name__ == "__main__":
    app.run()
