import mysql.connector

# Configurar la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'sibermotor'
}

# Conectar a la base de datos
conn = mysql.connector.connect(**db_config)

# Crear un cursor para ejecutar consultas
c = conn.cursor()

# Crear la tabla de productos
c.execute('''CREATE TABLE IF NOT EXISTS productos (codigo VARCHAR(50) PRIMARY KEY, nombre VARCHAR(50), precio DECIMAL(10, 2))''')

# Crear la tabla de transacciones
c.execute('''CREATE TABLE IF NOT EXISTS transacciones (id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(50), tipo VARCHAR(50), fecha DATETIME)''')

# Insertar un producto en la tabla de productos
c.execute("INSERT INTO productos (codigo, nombre, precio) VALUES (%s, %s, %s)", ('1234567890', 'Producto de prueba', 100.50))

# Insertar una transacción en la tabla de transacciones
c.execute("INSERT INTO transacciones (codigo, tipo, fecha) VALUES (%s, %s, NOW())", ('1234567890', 'ingreso'))

# Ejecutar una consulta
c.execute("SELECT * FROM productos")

# Obtener los resultados de la consulta
resultados = c.fetchall()

# Imprimir los resultados
for resultado in resultados:
    print(resultado)

# Cerrar la conexión a la base de datos
conn.close()