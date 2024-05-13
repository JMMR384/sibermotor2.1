import datetime
from typing import List, Dict

class Producto:
    def __init__(self, sku: str, descripcion: str, precio: float, stock: int, ubicacion: str):
        self.sku = sku
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.ubicacion = ubicacion

class Factura:
    def __init__(self, fecha: datetime.datetime, cliente: str, productos: List[Producto], total: float):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos
        self.total = total

    def generar_detalles(self) -> str:
        detalles = f"Factura generada el {self.fecha.strftime('%Y-%m-%d %H:%M')}\nCliente: {self.cliente}\n"
        for producto in self.productos:
            detalles += f"{producto.sku} - {producto.descripcion} - ${producto.precio} - Cantidad: {producto.stock}\n"
        detalles += f"Total: ${self.total}"
        return detalles

def crear_factura(cliente: str, productos: List[Producto]) -> Factura:
    total = sum([producto.precio * producto.stock for producto in productos])
    fecha = datetime.datetime.now()
    return Factura(fecha, cliente, productos, total)

def main():
    # Ejemplo de uso
    productos = [
        Producto("001", "Llanta de repuesto", 150.0, 5, "Almacén 1, Estante 3"),
        Producto("002", "Batería para auto", 200.0, 3, "Almacén 2, Estante 1"),
        Producto("003", "Faro delantero", 120.0, 7, "Almacén 1, Estante 1")
    ]
    factura = crear_factura("Cliente 1", productos)
    print(factura.generar_detalles())

if __name__ == "__main__":
    main()