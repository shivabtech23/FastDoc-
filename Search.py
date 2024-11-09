from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'r!$h!t0801',
    'database': 'HOSPITALS'
}


@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    specialization = request.args.get('specialization')
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT doctor_name, hospital_name, rating 
    FROM doctors 
    WHERE speciality = %s
    """
    cursor.execute(query, (specialization,))
    doctors = cursor.fetchall()

    cursor.close()
    connection.close()
    
    
    return render_template('anjali_cardiologist.html', doctors=doctors)


if __name__ == "__main__":
    app.run(debug=True)
