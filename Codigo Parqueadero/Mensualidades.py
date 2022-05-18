from multiprocessing.dummy.connection import Client
import Cliente
import Vehiculo

class Mensualidades:
    #Atributos
    TarifaDeMensualidades:int
    Vehiculo : Vehiculo
    
    def __init__(self, diadefacturacion:int, cliente:Cliente ):
        self.DiaDeFacturacion = diadefacturacion
        self.Cliente = cliente
    #Metodos
    def DefinirDiaDeFacturacion(self, DiaDeFacturacion):
        print("la fecha de facturacion es:", DiaDeFacturacion)

    def DefinirTarifaMensualidades(self, TarifaMensualidades):
        print("La tarifa de las mensualidades es:", TarifaMensualidades)