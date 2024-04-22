import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/characters", methods=["GET"])
def characters():
    return render_template("characters.html")


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/submit_login", methods=["POST"])
def submit_login():
    return render_template("index.html")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/submit_register", methods=["POST"])
def submit_register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    try:
        with open("data.json", "r") as infile:
            file_data = infile.read()
            if file_data.strip():
                data = json.loads(file_data)
            else:
                data = []
    except FileNotFoundError:
        data = []

    new_data = {"username": username, "email": email, "password": password}
    data.append(new_data)

    with open("data.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

    return redirect("/result")


@app.route("/result", methods=["GET"])
def result():
    try:
        with open("data.json", "r") as infile:
            file_data = infile.read()
            if file_data.strip():
                users = json.loads(file_data)
            else:
                users = []
    except FileNotFoundError:
        users = []

    return render_template("index.html", data=users)


if __name__ == "__main__":
    app.run(debug=True)
