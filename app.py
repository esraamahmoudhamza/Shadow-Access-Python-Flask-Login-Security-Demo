from flask import Flask, render_template, request

app = Flask(__name__)

# fake database
users = {
    "admin": "1234",
    "esraa": "pass"
}

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    print(f"[LOGIN ATTEMPT] {username} / {password}")

    if username in users and users[username] == password:
        message = f"ACCESS GRANTED 🔓 Welcome {username}"
        status = "success"
    else:
        message = "ACCESS DENIED ❌ Invalid Credentials"
        status = "fail"

    return render_template("login.html", message=message, status=status)


if __name__ == "__main__":
    app.run(debug=True)