from flask import Flask, render_template, request
from Database.database import init_db 
import sqlite3

app = Flask(__name__)   

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    patientname=request.form['name']
    patientemail=request.form['email']
    patientaddress=request.form['address']
    patientage=request.form['age']
    patientphone=request.form['phone']

    try:
        conn = sqlite3.connect('patient_information.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, address, age, phone) VALUES (?, ?, ?, ?, ?)', (patientname, patientemail, patientaddress, patientage, patientphone))
        conn.commit()
        conn.close()

        return f"""
        <h1>Submitted Information</h1>
        <p><b>Patient-Name:</b> {patientname}</p>
        <p><b>Patient-Email:</b> {patientemail}</p>
        <p><b>Patient-Address:</b> {patientaddress}</p>
        <p><b>Patient-Age:</b> {patientage}</p>
        <p><b>Patient-Phone:</b> {patientphone}</p>
        """
    except sqlite3.IntegrityError:
        return "<h1>Error: Email already exists!</h1>"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
