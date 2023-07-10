# app.py
import flask
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="accidents"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report_accident():
    if request.method == 'POST':
        location = request.form['location']
        date = request.form['date']
        time = request.form['time']

        # Save accident data to the database
        cursor = db.cursor()
        query = "INSERT INTO accidents (location, date, time) VALUES (%s, %s, %s)"
        values = (location, date, time)
        cursor.execute(query, values)
        db.commit()

        return "Accident reported successfully!"

    return render_template('report.html')

if __name__ == '__main__':
    app.run()

