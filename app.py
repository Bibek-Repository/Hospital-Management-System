from flask import Flask, render_template, request

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

    return f"""
    <h1>Submitted Information</h1>
    <p><b>Patient-Name:</b> {patientname}</p>
    <p><b>Patient-Email:</b> {patientemail}</p>
    <p><b>Patient-Address:</b> {patientaddress}</p>
    <p><b>Patient-Age:</b> {patientage}</p>
    <p><b>Patient-Phone:</b> {patientphone}</p>
    """
if __name__ == '__main__':
    app.run(debug=True)
