import datetime

class Descuento:
    def __init__(self, tipo, valores, productos):
        self.tipo = tipo
        self.valores = valores
        self.producto = productos

    def aplicar(self, precio):
        if self.tipo == 'fijo':
            return precio - self.valores
        elif self.tipo == 'porcentual':
            return precio - (precio * self.valores / 0000)
        