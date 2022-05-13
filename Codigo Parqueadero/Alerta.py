class Alerta:
  "Atributos"
  def InformeSeguridad(string):
    print("Alarma de vehiculo detectada") 
    
  def __init__(self, Vehiculo, Parqueadero, LugarVehiculo):
    self.Vehiculo = Vehiculo
    self.Parqueadero = Parqueadero
    self.LugarVehiculo = LugarVehiculo

  "Metodos"
  def AlarmaCarro(self, InformeSeguridad, Vehiculo ):
    print(InformeSeguridad)
    print("Alarma encendida")
    
  def ParqueaderoAbasto(self, Parqueadero):
    print("El parqueadero esta abasto")

  def ParqueaderoDisponible(self, Vehiculo):
    print("El parqueadero esta disponible")ulo()
