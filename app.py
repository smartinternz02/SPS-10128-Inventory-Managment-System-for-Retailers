from flask import Flask, render_template, request, url_for, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from re import match
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'AjqusjqnsjnuWGDgv53e2fwvdjwd6316F^D#^D#@'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root9408'
app.config['MYSQL_DB'] = 'jobportal'

mysql = MySQL(app)

# Primary Services


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        date = datetime.now()

        # Validating Data
        if len(name) < 3:
            msg = 'Length of name must be grater than 2 characters.'
            return render_template('contact.html', msg=msg)
        elif len(subject) < 10:
            msg = 'Subject must be grater than 10 characters'
            return render_template('contact.html', msg=msg)
        elif len(message) < 10:
            msg = 'Message must be grater than 10 characters'
            return render_template('contact.html', msg=msg)
        else:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO contacts (name, email, subject, messsage, date) VALUES (%s, %s, %s, %s, %s)', (name, email, subject, message, date))
            mysql.connection.commit()
            cursor.close()
            msg = 'We have successfully received your request.'
            return render_template('index.html', msg=msg)

    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')

# Registering new users


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = None
    data = None
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        mail = request.form['mail']
        contact = request.form['contact']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        check = request.form.get('t&c')
        # session['name'] = username

        if check == 'on':
            check = True
        else:
            check = False

        # Validation of data
        if len(name) < 3 or len(username) < 8:
            msg = 'Name must be greater than 2 chars and Username must greater than 8 chars'
            return render_template('register.html', msg=msg, valid=False)

        regex = "^(?=.{8, 20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$"
        if match(regex, username):
            msg = 'Only aA-Zz, 0-9, _ . allowed.'
            return render_template('register.html', msg=msg, valid=False)

        if len(password) < 8:
            msg = 'Password must be at least 8 characters long'
            return render_template('register.html', msg=msg,  valid=False)
        if password != confirmPassword:
            msg = 'Alert! Password Mismatch'
            return render_template('register.html', msg=msg,  valid=False)
        elif not check:
            msg = 'You must agree all T&Cs.'
            return render_template('register.html', msg=msg, check=check, valid=True)

        msg = 'successfully registered'
        data = [username, name, mail, contact, password, check]

        # Storing data to database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users(username, name, email, contact, password, agree) VALUES(%s, %s, %s, %s, %s, %s )',
                       (username, name, mail, contact, password, check))
        mysql.connection.commit()
        cursor.close()

        msg = 'successfully registered'
        data = [username, name, mail, contact, password, check]

    return render_template('register.html', success_msg=msg, data=data)


# Managing Authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    user_data = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        keep_alive = request.form.get('agree')

        if keep_alive == 'on':
            keep_alive = True
        else:
            keep_alive = False

        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT username, password from users where username = %s', (username,))
        mysql.connection.commit()
        user_data = cursor.fetchone()
        cursor.close()

        if user_data:
            if password == user_data[1]:
                session['username'] = username
                return render_template('index.html', session=session)
            else:
                msg = 'Password do not match'
                return render_template('login.html', msg=msg)

        else:
            msg = 'Sorry ! No such user exists.'
            return render_template('login.html', msg=msg)

    else:
        if 'username' in session:
            return redirect(url_for('index'))

    return render_template('login.html', user_data=user_data)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# Managing services
@app.route('/services')
def services():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM jobs')
    mysql.connection.commit()
    jobs = cursor.fetchall()
    cursor.close()
    rows = len(jobs)
    return render_template('services.html', jobs=jobs, rows=rows)


@app.route('/details')
def details():
    return render_template('details.html')


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if 'username' in session:
        msg = "You have successfully applied to this job."
        return render_template('services.html', msg=msg)
    else:
        msg = "You must login to apply to this job."
        return render_template('details.html', msg=msg)


# Running flask App
if __name__ == '__main__':
    app.run(debug=True)
