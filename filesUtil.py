import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Specify the file path and file name
file_path = 'P:\\Learning\\microservices\\1704257706495.gif'
file_name = '1704257706495.gif'

# Read the file as binary data
with open(file_path, 'rb') as file:
    file_data = file.read()

# Execute the SQL command to insert the file
cur.execute(
    "INSERT INTO files (name, data) VALUES (%s, %s)",
    (file_name, psycopg2.Binary(file_data))
)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
