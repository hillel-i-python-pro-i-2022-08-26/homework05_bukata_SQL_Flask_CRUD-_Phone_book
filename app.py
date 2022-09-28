from flask import Flask

from appllication.services import phone_table

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hi World!"


phone_table()


if __name__ == "__main__":
    app.run()
