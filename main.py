from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Job
import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"

db_session.global_init("db/mars_explorer.db")


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return render_template("index.html", jobs=jobs)


def main():
    app.run()


if __name__ == "__main__":
    main()
