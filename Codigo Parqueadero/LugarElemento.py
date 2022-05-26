import Elementos
import Parqueadero

class LugarElemento:
	#Atributos 
	Elementos : Elementos
	Parqueadero : Parqueadero
	DefinirElLugarDelElemento : str

	def __init__(self, EspaciosParaAlmacenarElementos:int ):
		self.EspaciosParaAlmacenarElementos:int

	#Metodos
	def DestinarUnSitioDeElemento(self):
		print("Mostrar sitio del elemento")