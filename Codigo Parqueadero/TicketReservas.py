import Reservas
import LugarParqueadero

class TicketReservas:
    #Atributos
    def __init__(self, reservas:Reservas, lugarparqueadero:LugarParqueadero):
        self.Reservas = reservas
        self.LugarParqueadero = lugarparqueadero

    #Metodos
    def DefinirLugarDeRerva(lugarParqueadero):
        print("Su lugar de reserva es", lugarParqueadero)

    def ImprimirTicketReserva(self):
        print(LugarParqueadero,Reservas)