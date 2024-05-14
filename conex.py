import mysql.connector
# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sibermotor"
)

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