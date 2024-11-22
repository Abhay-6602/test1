from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection function
def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

# Function to create the necessary table
def create_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email TEXT UNIQUE,
            phone_number TEXT,
            gender TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Admin function to fetch all user data
def admin():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users2')
    data = cur.fetchall()
    conn.close()
    return data

# Routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate user credentials
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users2 WHERE email = ? AND password = ?", (email, password))
        user = cur.fetchone()
        conn.close()

        if user:
            return "Login successful! Welcome, " + user[1]
        else:
            return "Invalid credentials. Please <a href='/login'>try again</a>."
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get("full_name")
        phone_number = request.form.get("phone_number")
        email = request.form.get("email")
        gender = request.form.get("gender")
        password = request.form.get("password")


        # if password != confirm_password:
        #     return "Passwords do not match. Please <a href='/register'>try again</a>."

        conn = create_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO users2 (full_name, email, phone_number, gender, password) VALUES (?, ?, ?, ?, ?)",
                (full_name, email, phone_number, gender, password)
            )
            conn.commit()
            conn.close()
            return redirect("/login")
        except sqlite3.IntegrityError:
            conn.close()
            return "Email already exists. Please <a href='/register'>try again</a>."
    return render_template('registration.html')

if __name__ == '__main__':
    create_table()  # Ensure the table exists before starting the app
    app.run(debug=True)
