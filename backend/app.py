from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your_secret_key'

# Enter your database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'ticket_system'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['role'] = account['role']
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username / password!')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = request.form.get('role', 'user')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            flash('Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!')
        elif not username or not password or not email:
            flash('Please fill out the form!')
        else:
            hashed_password = generate_password_hash(password)
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s)', (username, hashed_password, email, role))
            mysql.connection.commit()
            flash('You have successfully registered!')
            return redirect(url_for('login'))
    elif request.method == 'POST':
        flash('Please fill out the form!')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM tickets WHERE user_id = %s', (session['id'],))
        tickets = cursor.fetchall()
        return render_template('dashboard.html', tickets=tickets)
    return redirect(url_for('login'))

@app.route('/raise_ticket', methods=['GET', 'POST'])
def raise_ticket():
    if 'loggedin' in session:
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            priority = request.form['priority']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO tickets (user_id, title, description, priority, status) VALUES (%s, %s, %s, %s, %s)', 
                           (session['id'], title, description, priority, 'open'))
            mysql.connection.commit()
            flash('Ticket raised successfully!')
            return redirect(url_for('dashboard'))
        return render_template('raise_ticket.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)