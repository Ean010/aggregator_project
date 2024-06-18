import sqlite3
from scrape_the_verge import scrape_the_verge_titles

def store_titles_in_db(titles):
    conn = sqlite3.connect('pagedatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS titles (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    link TEXT,
                    date TEXT
                )''')
    
    c.executemany('INSERT INTO titles (title, link, date) VALUES (?, ?, ?)',
                  [(title, link, date.strftime('%Y-%m-%d')) for title, link, date in titles])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    titles = scrape_the_verge_titles()
    store_titles_in_db(titles)
    print("Titles stored in database.")
