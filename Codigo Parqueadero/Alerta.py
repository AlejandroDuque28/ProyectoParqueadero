import Vehiculo
import Parqueadero
import LugarVehiculo

class Alerta:
  def InformeSeguridad(string):
    print("Alarma de vehiculo detectada") 
    
  def __init__(self):
    self.Vehiculo = Vehiculo
    self.Parqueadero = Parqueadero
    self.LugarVehiculo = LugarVehiculo

  def AlarmaCarro(self):
    print(InformeSeguridad)
    print("Alarma encendida")
    
  def ParqueaderoAbasto(self):
    print("El parqueadero esta abasto")

  def ParqueaderoDisponible(self):
    print("El parqueadero esta disponible")