from flask import Flask, render_template, request
from recommender import recommend_schemes

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    user = {
        "age": int(request.form["age"]),
        "gender": request.form["gender"],
        "category": request.form["category"],
        "income": int(request.form["income"]),
        "student": request.form["student"],
        "farmer": request.form["farmer"],
        "disability": request.form["disability"]
    }

    schemes = recommend_schemes(user)

    return render_template("result.html", schemes=schemes)


if __name__ == "__main__":
    app.run(debug=True)
