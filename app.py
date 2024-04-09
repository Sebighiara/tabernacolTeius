from flask import Flask, render_template, abort, redirect
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('presentations.db')

#Function to fetch videos from the database
def get_videos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM youtubeVideos")
    videos = cursor.fetchall()
    conn.close()
    return videos

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
    try:
        videos_data = get_videos()
        return render_template("index.html", videos=videos_data)
    except Exception as e:
        abort(404)

# Route to render the presentations page
@app.route("/presentations")
def presentations():
    try:
        presentations_data = get_presentations()
        return render_template("presentations.html", presentations=presentations_data)
    except Exception as e:
        abort(404)

@app.route('/download/<path:presentation_url>')
def download_presentation(presentation_url):
    return redirect(presentation_url)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)