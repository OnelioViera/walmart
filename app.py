from flask import (
    Flask,
    render_template,
    request,
    session,
    flash,
    make_response,
    redirect,
)


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

users = {}  # Placeholder to store user information


@app.route("/")
def base():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Perform login process
        username = request.form["username"]
        password = request.form["password"]

        # Validate username and password
        if username in users and users[username] == password:
            # Set Session variables or user tokens for authentication purposes
            session["logged_in"] = True
            session["username"] = username
            flash("Login successful!")
            return render_template(
                "login.html",
            )
        else:
            flash("Invalid username or password!")

    return render_template("login.html")
