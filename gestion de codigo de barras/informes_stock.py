import cv2
import sqlite3
from pyzxing import BarcodeFormat, Reader

# Inicializar el lector de códigos de barras
reader = Reader()

# Conectar a la base de datos
conn = sqlite3.connect('productos.db')
c = conn.cursor()

def registrar_producto(codigo, nombre, precio):
    # Insertar el producto en la tabla de productos
    c.execute("INSERT INTO productos (codigo, nombre, precio) VALUES (?, ?, ?)", (codigo, nombre, precio))

    conn.commit()

def registrar_transaccion(codigo, tipo):
    # Obtener el precio del producto
    c.execute("SELECT precio FROM productos WHERE codigo=?", (codigo,))
    precio = c.fetchone()[0]

    # Insertar la transacción en la tabla de transacciones
    c.execute("INSERT INTO transacciones (codigo, tipo, fecha) VALUES (?, ?, datetime('now'))", (codigo, tipo))

    conn.commit()

    return precio

def leer_codigo_barras(imagen=None):
    # Leer el código de barras desde una imagen o la cámara web
    if imagen is None:
        # Abrir la cámara web
        cap = cv2.VideoCapture(0)

        # Leer el código de barras desde la cámara web
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Decodificar el código de barras
            result = reader.decode(frame, formats=[BarcodeFormat.QR_CODE, BarcodeFormat.CODE_128])
            if result is not None:
                codigo = result.text
                cv2.imshow('Código de barras', frame)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()
                cap.release()
                return codigo

    else:
        # Leer el código de barras desde una imagen
        result = reader.decode(imagen, formats=[BarcodeFormat.QR_CODE, BarcodeFormat.CODE_128])
        if result is not None:
            codigo = result.text
            return codigo

def generar_informe():
    # Obtener los datos de las transacciones
    c.execute("SELECT codigo, tipo, fecha FROM transacciones ORDER BY fecha")
    transacciones = c.fetchall()

    # Agrupar las transacciones por código de barras
    productos = {}
    for transaccion in transacciones:
        codigo, tipo, fecha = transaccion
        if codigo not in productos:
            productos[codigo] = {'ingresos': 0, 'ventas': 0, 'precio': None, 'ultima_transaccion': None}
        if tipo == 'ingreso':
            productos[codigo]['ingresos'] += 1
            productos[codigo]['precio'] = registrar_transaccion(codigo, tipo)
            productos[codigo]['ultima_transaccion'] = fecha
        elif tipo == 'venta':
            productos[codigo]['ventas'] += 1

    # Imprimir el informe
    print("Código de barras | Ingresos | Ventas | Precio | Última transacción")
    for codigo, datos in productos.items():
        print(f"{codigo} | {datos['ingresos']} | {datos['ventas']} | ${datos['precio']} | {datos['ultima_transaccion']}")

# Ejemplo de uso
# Registrar un producto
registrar_producto('1')