
from questions import *
import requests
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/json")
def jsonit():
    data = jsonify(questions)
    return data


@app.route("/")
def start():
    q1 = questions[0]["question"]
    q2 = questions[1]["question"]
    q3 = questions[2]["question"]
    print(q1, q2, q3)
    return render_template("challenge.html", q1=q1, q2=q2, q3=q3, questions=questions)


@app.route("/trivia", methods=["GET", "POST"])
def trivia():
    if request.method == "POST":
        ans1 = request.form.get("q1answer")
        ans2 = request.form.get("q2answer")
        ans3 = request.form.get("q3answer")

        return render_template("result.html",
                               q1answer=ans1, q2answer=ans2, q3answer=ans3, questions=questions)

    if request.method == "GET":
        ans1 = request.args.get("q1answer")
        ans2 = request.args.get("q2answer")
        ans3 = request.args.get("q3answer")
        print(ans1, ans2, ans3)
        if ans1 is None or ans2 is None or ans3 is None:
            return redirect(url_for("start"))
        else:
            return render_template("result.html",
                                   q1answer=ans1, q2answer=ans2, q3answer=ans3, questions=questions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
