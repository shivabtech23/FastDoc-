from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mail import Mail, Message
import mysql.connector
from mysql.connector import Error
import hashlib
from datetime import timedelta

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'your_secret_key' 
app.permanent_session_lifetime = timedelta(minutes=30)  


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'AroraShiv1!',
    'database': 'HOSPITALS3'
}

# Flask-Mail configuration for Gmail
app.config['MAIL_SERVER'] = 'live.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = 'cfdd98ab36199f07e3070bfe64edc5bd'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)


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
                conn.close()
                return redirect(url_for('home'))
            else:
                flash("Invalid email or password.")
                conn.close()
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
                conn.close()
                return redirect(url_for('login'))


            sql = "INSERT INTO Users (FullName, PhoneNumber, Age, Gender, Email, Passcode) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (full_name, phone, age, gender, email, hashed_password))
            conn.commit()
            flash("Registration successful! Please log in.")
            conn.close()
            return redirect(url_for('login'))

        flash("Database connection error.")
        return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.")
    return redirect(url_for('login'))


@app.route('/dr_dr._anjali_reddy.html')
def dr_anjali_reddy():
    return render_template('dr_anjali_reddy.html')

@app.route('/dr_dr.Pallavi_k.html')
def dr_aarti_malhotra():
    return render_template('Pallavi_k.html')

@app.route('/dr_dr.Vikram.s.html')
def dr_karan_gupta():
    return render_template('Vikram.s.html')

@app.route('/dr_dr.Sunil_s.html')
def dr_kavita_pandey():
    return render_template('Sunil_s.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    selected_date = data.get('date')
    selected_time = data.get('time')

    if not selected_date or not selected_time:
        return jsonify({'status': 'error', 'message': 'Date or time not provided.'})

    
    msg = Message(
        'Booking Confirmed',
        sender='hi@demomailtrap.com',
        recipients=['resqservices12@gmail.com']
    )
    
    msg.body = f'Your booking with the doctor has been confirmed for {selected_date} at {selected_time}. For further queries kindly contact us via our Customer support Email: resqservices12@gmail.com or Phone number: +9198203840274'

    try:
        mail.send(msg)
        return jsonify({'status': 'success', 'message': 'Email has been sent!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/api/doctors', methods=['GET'])
def search_doctors():
    specialization = request.args.get('specialization')
    hospital_name = request.args.get('hospital')
    sort_by_rating = request.args.get('sort_by_rating')

    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    
    query = "SELECT doctor_name, hospital_name, rating FROM doctors WHERE 1=1"
    params = []

    
    if specialization:
        query += " AND speciality = %s"
        params.append(specialization)
    
    if hospital_name:
        query += " AND hospital_name = %s"
        params.append(hospital_name)
    
    
    if sort_by_rating == 'true': 
        query += " ORDER BY rating DESC"
    else:
        query += " ORDER BY rating DESC"

    cursor.execute(query, tuple(params))
    results = cursor.fetchall()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
