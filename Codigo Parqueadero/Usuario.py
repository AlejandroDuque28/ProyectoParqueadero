class Usuario:
    #Atributos
    Cedula: int
    Telefono: int
    Direccion: str
    def __init__(self, nombre:str, contrasenia:str):
        self.Nombre = nombre
        self.Contrasenia = contrasenia

    #Metodos
    def IniciarSesion(Nombre, Contrasenia):
        print("Iniciando Sesion")

    def Registrar(self):
        pass
