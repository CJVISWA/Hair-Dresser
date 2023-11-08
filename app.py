from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector

# Configure app
app = Flask(__name__)

# Define a variable for the MySQL connection
mydb = None

# Configure MySQL connection
try:
    mydb = mysql.connector.connect(
        host="hairdresser.c21fafpar6xm.eu-north-1.rds.amazonaws.com",
        user="cj",
        password="viswacj123",
        database="hairdresser"
    )
except Exception as e:
    print(e)

if mydb:
    mycursor = mydb.cursor()
else:
    print("MySQL connection failed. Check your connection parameters.")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        if (username == "Viswa" and password == "cj1") or (username == "Venky" and password == "cj2"):
            return render_template("shop_register.html", username=username)

    return "Hello, you don't have access permission"


@app.route("/shop_register", methods=["GET", "POST"])
def shop_register():
    if request.method == "GET":
        try:
            mycursor.execute("SELECT * FROM shop")
            rows = mycursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        return render_template("shop_list.html", rows=rows)
    else:
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

        sql = "INSERT INTO shop(shop_name, branch, working_days, leave_day, username, password, mobile, email, gender, seats, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (shop_name, branch, working_days, leave_day, username, password_hashed, mobile_no, email, gender, seats, address)

        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("SELECT * FROM shop")
        rows = mycursor.fetchall()
        return render_template("shop_list.html", rows=rows)
