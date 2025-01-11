from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# MySQL database configuration using environment variables
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME')
}

# Function to get a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        if 'submit' in request.form:  # Check if it's the "Submit" button
            name = request.form['name']
            email = request.form['email']
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
        elif 'delete' in request.form:  # Check if it's the "Delete" button
            user_index = int(request.form['index'])
            cursor.execute("DELETE FROM users WHERE id = %s", (user_index,))
            conn.commit()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('user_list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')