import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('movies.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "movies" table
cursor.execute('''CREATE TABLE movies
                  (year INTEGER, title TEXT, genre TEXT)''')

# Define the data to be inserted
data = [
    (2009, 'Brothers', 'Drama'),
    (2002, 'Spider Man', 'Sci-fi'),
    (2009, 'WatchMen', 'Drama'),
    (2010, 'Inception', 'Sci-fi'),
    (2009, 'Avatar', 'Fantasy')
]

# Insert the data into the "movies" table
cursor.executemany('INSERT INTO movies VALUES (?, ?, ?)', data)

# Commit the changes and close the connection
conn.commit()
conn.close()
