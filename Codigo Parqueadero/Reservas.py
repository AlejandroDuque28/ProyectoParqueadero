import Vehiculo
import Usuario
import Parqueadero

class Reservas:
    def Email(string):
        input("Ingrese Su Correo: ")
    def FechaReserva(string):
        input("Ingrese La Fecha De Reserva: ")
    def HoraReserva(string):
        input("Ingrese La Hora De Reserva: ")
    def __init__(self):
        self.Vehiculo = Vehiculo()
        self.Usuario = Usuario()
        self.Parqueadero = Parqueadero()

    def DefinirReserva(self):
        print("Reserva Realizada")

    def DestinarUnLugarDeParqueo(Parqueadero):
        print("El lugar de su reserva es: ", Parqueadero)