from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  


def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='AroraShiv1!', 
            database='USER'
        )
        if conn.is_connected():
            print("Connected to MySQL database")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None


def hash_password(passcode):
    return hashlib.sha256(passcode.encode()).hexdigest()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = create_connection()
        if conn:
            email = request.form['email']
            passcode = request.form['passcode']
            hashed_password = hash_password(passcode)

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE Email = %s AND Passcode = %s", (email, hashed_password))
            user = cursor.fetchone()

            if user:
                session['user'] = user[1] 
                flash(f"Welcome back, {user[1]}!")
                return redirect(url_for('home'))
            else:
                flash("Invalid email or password.")
                return redirect(url_for('login'))

        flash("Database connection error.")
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = create_connection()
        if conn:
            full_name = request.form['full_name']
            phone = request.form['phone']
            age = int(request.form['age'])
            gender = request.form['gender']
            email = request.form['email']
            passcode = request.form['passcode']
            hashed_password = hash_password(passcode)

            cursor = conn.cursor()

         
            cursor.execute("SELECT * FROM Users WHERE Email = %s OR PhoneNumber = %s", (email, phone))
            if cursor.fetchone():
                flash("An account with this email or phone number already exists. Please log in.")
                return redirect(url_for('login'))

       
            sql = "INSERT INTO Users (FullName, PhoneNumber, Age, Gender, Email, Passcode) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (full_name, phone, age, gender, email, hashed_password))
            conn.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for('login'))

        flash("Database connection error.")
        return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('user', None) 
    flash("You have been logged out.")
    return redirect(url_for('login')) 

if __name__ == '__main__':
    app.run(debug=True)
