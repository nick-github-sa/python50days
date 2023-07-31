import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('movies.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute("DELETE FROM movies")

# Commit the changes and close the connection
conn.commit()
conn.close()
