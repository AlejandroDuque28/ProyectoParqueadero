import Elementos
import Parqueadero

class LugarElemento:
	def EspaciosParaAlmacenarElementos(string):
		print("Escoger espacio para el elemento")

	def DefinirElLugarDelElemento(string):
		print("Definir un lugar para el elemento")

	def __init__(self):
		self.Elementos = Elementos
		self.Parqueadero = Parqueadero

	def DestinarUnSitioDeElemento(self):
		print("Mostrar sitio del elemento")