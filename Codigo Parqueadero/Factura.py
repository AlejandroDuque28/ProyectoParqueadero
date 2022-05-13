import Vehiculo
import Usuario
import Tiempo
import Tarifa
import MetodoPago

class Factura:
	def __init__(self):
		self.Usuario = Usuario
		self.Tiempo = Tiempo
		self.Tarifa = Tarifa
		self.MetodoPago = MetodoPago
		self.Vehiculo = Vehiculo

	def ImprimirFactura(self):
		print("Imprimir datos factura")
