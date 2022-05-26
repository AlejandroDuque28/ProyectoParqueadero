import Vehiculo
import Parqueadero
import LugarVehiculo

class Alerta:
<<<<<<< HEAD
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
=======
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
>>>>>>> f5a7da26f3f470475aa38beb43f1217cfdd4ce83
