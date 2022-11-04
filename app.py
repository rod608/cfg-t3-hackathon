from flask import Flask, render_template, request, redirect

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
       first_name = request.form.get("1. What level of education does you belong to?")
       # getting input with name = lname in HTML form
       last_name = request.form.get("2.  How much time are you able to spend pursuing an educational program?")
       return "Your name is "+first_name + last_name
    
