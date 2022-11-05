from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def welcome():
    return render_template("index-quiz.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
