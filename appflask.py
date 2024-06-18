import sqlite3

def check_table_existence():
    conn = sqlite3.connect('pagedatabase.db')
    c = conn.cursor()

    # Query to check if the table 'titles' exists
    c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='titles';''')
    table_exists = c.fetchone()

    conn.close()

    return table_exists is not None

def get_titles_from_db():
    if not check_table_existence():
        # Handle case where the table does not exist
        print("Table 'titles' does not exist in the database.")
        return []

    conn = sqlite3.connect('pagedatabase.db')
    c = conn.cursor()
    c.execute('SELECT title, link, date FROM titles ORDER BY date DESC')
    titles = c.fetchall()
    conn.close()
    return titles

# Example usage in Flask app
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titles = get_titles_from_db()
    return render_template('pageAggregator.html', titles=titles)

if __name__ == "__main__":
    app.run(debug=True)
