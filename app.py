from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def welcome():
    
    # the user has not filled out the quiz yet
    if request.method == "GET":
        return render_template("index-quiz.html")
    
    # the user has filled out the quiz
    if request.method == "POST":
        # the user has filled out the quiz and we want to display proper pathway resources
        # return render_template("propertemplate.html")
        first_answer = request.form.get("q1")
        second_answer = request.form.get("q2")
        third_answer = request.form.get("q3")
        schools = pd.read_csv("T3Data.csv")
        schools = schools[schools["Grade"] == first_answer]
        schools = schools[schools["Time_Available"] == second_answer]
        schools = schools[schools["Finances"] == third_answer]
        schools.rename(columns = {"Cost(3 diff ranges, annual)": "Cost"}, inplace = True)
        schools["link"] = schools["link"].apply(lambda x: "<a href="+x+">Cost Information</a>")
        return render_template("result.html", schools=schools)


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
