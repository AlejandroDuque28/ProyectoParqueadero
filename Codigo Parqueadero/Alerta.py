import Vehiculo
import Parqueadero
import LugarVehiculo

class Alerta:
    #Atributos
    InformeSeguridad : str

    
    def __init__(self, Vehiculo:Vehiculo, Parqueadero:Parqueadero, LugarVehiculo:LugarVehiculo):
      self.Vehiculo = Vehiculo
      self.Parqueadero = Parqueadero
      self.LugarVehiculo = LugarVehiculo


    #Metodos
    def AlarmaCarro(self):
      print(InformeSeguridad)
      print("Alarma encendida")
    
    def ParqueaderoAbasto(self):
      print("El parqueadero esta abasto")

    def ParqueaderoDisponible(self):
      print("El parqueadero esta disponible")