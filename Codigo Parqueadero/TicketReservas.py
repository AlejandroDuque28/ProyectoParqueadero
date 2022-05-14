import Reservas
import LugarParqueadero

class TicketReservas:
    def __init__(self):
        self.Reservas = Reservas
        self.LugarParqueadero = LugarParqueadero

    def DefinirLugarDeRerva(lugarParqueadero):
        print("Su lugar de reserva es", lugarParqueadero)

    def ImprimirTicketReserva(self):
        print(LugarParqueadero,Reservas)