from flask import Flask, render_template, redirect, request, session, url_for
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

db = SQL("sqlite:///bettermuslim.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return "Username cannot be blank"
        if not password:
            return "Password cannot be blank"
        if confirmation != password:
            return "Password doesn't match"
        
        db.execute("INSERT INTO users (username, hash, cash) VALUES(?, ?, 0)", username, generate_password_hash(password))
        return redirect("/login")

    else:
        return render_template("register.html")
        
@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        
        # Ensure username was submitted
        if not request.form.get("username"):
            return "must provide username"

        # Ensure password was submitted
        elif not request.form.get("password"):
            return "must provide password"

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return "invalid username and/or password"

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")

@app.route("/")
def index():
    if session.get("user_id") == None:
        return redirect("/login")
    else:
        name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
        return render_template("index.html", name=name[0]["username"])

@app.route("/resources")
def resources():
    if session.get("user_id") == None:
        return redirect("/login")
    else:
        return render_template("resources.html")

@app.route("/todolists", methods=["GET", "POST"])
def todolists():
    if session.get("user_id") == None:
        return redirect("/login")
    else:
        if request.method == "POST":
            task = request.form.get("toDoInput")
            db.execute("INSERT INTO todolist (task, status, userid) VALUES(?, 0, ?)", task, session["user_id"])
            return redirect("/todolists")
        else:
            todolists = db.execute("SELECT * FROM todolist WHERE userid = ?", session["user_id"])
            return render_template("todolists.html", todolists=todolists)

@app.route("/editodo", methods=["GET", "POST"])
def editodo():
    if session.get("user_id") == None:
        return redirect("/login")
    else:
        if request.method == "POST":
            data = request.form.get("delete")
            db.execute("DELETE FROM todolist WHERE id = ?", data)
            return redirect("/todolists")
        else:
            return redirect("/todolists")

@app.route("/donations", methods=["GET", "POST"])
def donations():
    if session.get("user_id") == None:
        return redirect("/login")
    else:
        if request.method == "POST":
            amount = request.form.get("cashAmount")
            db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", int(amount), session["user_id"])
            return redirect("/donations")
        else:
            wallet = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            return render_template("donations.html", wallet=wallet[0]["cash"])
        
@app.route("/donate", methods=["GET", "POST"])
def donate():
    if session.get("user_id") == None:
        return redirect("/login")
    else:
        if request.method == "POST":
            dono = request.form.get("donoAmount")
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", dono, session["user_id"])
            return redirect("/donations")
        else:
            return redirect("/donations")
