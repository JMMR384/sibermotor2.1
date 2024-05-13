class Promocion:
    def __init__(self, condicion, descuento, productos):
        self.condicion = condicion
        self.descuento = descuento
        self.productos = productos

    def cumple_condicion(self, fecha, productos):
        return True

    def aplicar(self, productos):
        precios_originales = {producto.sku: producto.precio for producto in productos}
        for producto in productos:
            if producto.sku in self.productos:
                descuento = self.descuento.aplicar(precios_originales[producto.sku])
                producto.precio = descuento