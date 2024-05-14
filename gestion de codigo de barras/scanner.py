# Connect to the database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sibermotor"
    )
except mysql.connector.Error as e:
    print(f"Error connecting to database: {e}")
    exit()

# Create a cursor object
c = conn.cursor()

# Insert a new product into the database
nombre = "Product name"
precio = 10
c.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", (nombre, precio))

# Commit the transaction and close the cursor object
conn.commit()
c.close()

# Close the database connection
conn.close()