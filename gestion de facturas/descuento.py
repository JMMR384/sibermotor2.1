import datetime

class Descuento:
    def __init__(self, tipo, valor, producto):
        self.tipo = tipo
        self.valor = valor
        self.producto = producto

    def aplicar(self, precio):
        if self.tipo == 'fijo':
            return precio - self.valor