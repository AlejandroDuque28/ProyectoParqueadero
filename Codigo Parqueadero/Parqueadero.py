# -*- coding: utf-8 -*-
"""Parqueadero (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O75nHSqZC3quY70YX_rCKvO1UGP3bLcM
"""
import LugarParqueadero
import Alerta

class Parqueadero:
    "atributos"
    def __init__(self,Alerta:Alerta, LugarParqueadero:LugarParqueadero, numeroDeParqueaderos:int, numeroDePisosDeParqueadero:int):
      self.Alerta = Alerta
      self.LugarParqueadero = LugarParqueadero
      self.numeroDeParqueaderos = numeroDeParqueaderos
      self.numeroDePisosDeParqueadero = numeroDePisosDeParqueadero

    "metodos"
    def RegistrarElTotalDeEspaciosDelParqueadero(self, numeroDeParqueaderos):
        print("numero de parqueaderos que hay en el parqueadero",numeroDeParqueaderos)
    
    def RegistrarNumeroDePisosDeParqueaderos(self, numeroDePisosDeParqueadero):
        print("el numero de pisos de parqueos",numeroDePisosDeParqueadero)