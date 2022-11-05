from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
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
        return "Your name is "+ first_answer + second_answer + third_answer
    
