class Factura(Vehiculo, ListaTransferenciasbancarias):
	def __init__(self, Usuario, Tiempo, Tarifa, MetodoPago):
		self.Usuario = Usuario
		self.Tiempo = Tiempo
		self.Tarifa = Tarifa
		self.MetodoPago = MetodoPago
		self.Vehiculo = Vehiculo

    def ImprimirFactura(self, Tiempo, Tarifa):
    	return self.Tarifa * self.Tiempo 
    	print("Imprimir datos factura")
