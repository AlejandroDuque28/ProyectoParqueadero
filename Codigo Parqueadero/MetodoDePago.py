import ListaTransferenciasbancarias

class MetodoDePago:
	#Atributos
	def __init__(self, Efectivo:Efectivo, ListaTransferenciasbancarias:lista):
		self.Efectivo = Efectivo
		self.ListaTransferenciasbancarias = lista

	#Metodos
	def DeterminarMetodoPag(self):
		print("Metodos de pago seleccionado por el usuario")
