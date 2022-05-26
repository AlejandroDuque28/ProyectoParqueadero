import Vehiculo
import Usuario
import Tiempo
import Tarifa
import MetodoPago

class Factura:
	#Atributos
	Usuario:Usuario

	def __init__(self, Vehiculo:Vehiculo, Tiempo:Tiempo, Tarifa:Tarifa, MetodoPago:MetodoPago):
		self.Vehiculo = Vehiculo
		self.Tiempo = Tiempo
		self.Tarifa = Tarifa
		self.MetodoPago = MetodoPago
		
	#Metodos
	def ImprimirFactura(self):
		print("Imprimir datos factura")
