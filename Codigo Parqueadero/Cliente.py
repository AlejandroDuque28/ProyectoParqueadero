from Usuario import Usuario

class Cliente(Usuario):
    #Atributos
    def __init__(self, usuario:Usuario):
        self.Usuario = usuario
    #Metodos
    def Cedula(int):
        int(input("Digite su cedula"))

    def Contrasenia(string):
        input("Digite su contraseña")


    def Registrar(self):
        return super().Registrar(self.Cedula, self.Contrasenia)

