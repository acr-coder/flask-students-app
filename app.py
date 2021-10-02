from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
import psycopg2 
import psycopg2.extras



app = Flask(__name__)
app.secret_key = "aaa_bbb"

conn = psycopg2.connect(user="postgres",
                        password = "wD5pem$n",
                        host= "localhost",
                        port = "5432",
                        database="mytestdb")

@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM students"
    cur.execute(s)
    list_students = cur.fetchall()
    return render_template('index.html', list_students = list_students)

@app.route('/add_student', methods=['POST'])
def add_student():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        cur.execute("INSERT INTO students (fname, lname, email) VALUES (%s,%s,%s)",(fname,lname,email))
        conn.commit()
        flash('Student added successfully')
        return redirect(url_for('Index'))



if __name__ == "__main__":
    app.run(debug=True)