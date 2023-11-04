from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from helpers import apology
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)
 
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///hair.db")

@app.route("https://cjviswa.github.io/Hair-Dresser/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        if (username == "Viswa" and password == "cj1") or (username == "Venky" and password == "cj2"):
            return render_template("shop_register.html",username=username)
        
    return apology(f"Hello {username} you dont have access permission", 403)


@app.route("/shop_register", methods=["POST"])
def shop_register():
    shop_name = request.form.get("shop_name")
    branch = request.form.get("branch")
    working_days = request.form.get("working_days")
    leave_day = request.form.get("leave_day")
    username = request.form.get("username")
    password = request.form.get("password")
    mobile_no = request.form.get("mobile_no")
    email = request.form.get("email")
    gender = request.form.get("gender")
    seats = request.form.get("seats")
    address = request.form.get("address")

    password_hashed = generate_password_hash(password)

    db.execute(
            "INSERT INTO shop(shop_name, branch, working_days, leave_day, username, password, mobile, email, gender, seats, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
            shop_name, branch, working_days, leave_day, username, password_hashed, mobile_no, email, gender, seats, address
            )

    rows = db.execute("SELECT * FROM shop")
    
    return render_template("shop_list.html", rows=rows)
