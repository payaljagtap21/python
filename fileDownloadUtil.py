import psycopg2

# Database connection details
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Define the ID of the file you want to download
file_id = 10

# Execute the SQL command to fetch the file data
cur.execute("SELECT name, data FROM files WHERE id = %s", (file_id,))

# Fetch the result
file = cur.fetchone()

# Check if a file was found
if file:
    file_name, file_data = file
    # Write the binary data to a file
    with open(file_name, 'wb') as f:
        f.write(file_data)
    print(f"File {file_name} has been downloaded successfully.")
else:
    print("No file found with the specified ID.")

# Close the cursor and connection
cur.close()
conn.close()
