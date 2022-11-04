from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def welcome():
    
    return render_template("homepage.html")
