import Vehiculo
import Usuario
import Parqueadero

class Reservas:
    #Atributos
    Email:str
    Parqueadero: Parqueadero

    def __init__(self, vehiculo:Vehiculo, usuario:Usuario, fechareserva:str, horareserva:str):
        self.Vehiculo = vehiculo
        self.Usuario = usuario
        self.FechaReserva = fechareserva
        self.HoraReserva = horareserva
    #Metodos
    def DefinirReserva(self):
        print("Reserva Realizada")

    def DestinarUnLugarDeParqueo(Parqueadero):
        print("El lugar de su reserva es: ", Parqueadero)