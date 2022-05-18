from Usuario import Usuario


class Administrador(Usuario):
    #Atributos
    def __init__(self, idvigilante:int, contraseniavigilante:str):
        self.IdVigilante = idvigilante
        self.ContraseniaVigilante = contraseniavigilante

    #Metodos
    def Registrar(self):
        return super().Registrar(self.IdVigilante, self.ContraseniaVigilante)

        
    
