from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

users = {}  # Placeholder to store user information


@app.route("/")
def base():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve the email from the login form
        email = request.form["email"]

        # Store the email in the session
        session["email"] = email

        return redirect("/registration")

    return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # Retrieve form data
        email = request.form["email"]
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        password = request.form["newPassword"]

        # Perform registration logic here (e.g., store user information in database)
        # Replace this with your own implementation

        # Render a success page or redirect to a different page
        return render_template("success.html")

    # Retrieve the email from the session
    email = session.get("email")

    # Render the registration form
    return render_template("registration.html", email=email)


if __name__ == "__main__":
    app.run(debug=True)
