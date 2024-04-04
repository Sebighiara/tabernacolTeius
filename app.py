from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('presentations.db')

# Function to fetch presentations from the database
def get_presentations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM presentations")
    presentations = cursor.fetchall()
    conn.close()
    return presentations

@app.route("/")
def home():
    return render_template("index.html")

# Route to render the presentations page
@app.route("/presentations")
def presentations():
    try:
        presentations_data = get_presentations()
        return render_template("presentations.html", presentations=presentations_data)
    except Exception as e:
        abort(404)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)