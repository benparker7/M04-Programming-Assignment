import sqlite3
import csv

books2 = [
    ['The Weirdstone of Brisingamen', 'Alan Garner', 1960],
    ['Perdido Street Station', 'China Miéville', 2000],
    ['Thud!', 'Terry Pratchett', 2005],
    ['The Spellman Files', 'Lisa Lutz', 2007],
    ['Small Gods', 'Terry Pratchett', 1992]
    ]
with open('books2.csv', 'r') as f_out:
    csv_out = csv.reader(f_out)


connection = sqlite3.connect('books.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE books
(title TEXT, author TEXT, year INTEGER)''')
cursor.executemany('INSERT INTO books VALUES (?, ?, ?)', books2)
cursor.execute('SELECT title FROM books ORDER BY title')
fetch = cursor.fetchall()
print(fetch)
