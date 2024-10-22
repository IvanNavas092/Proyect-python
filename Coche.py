# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:16:04 2024

@author: navas
"""

# %% POO
class Coche:
    
    def __init__(self, marca, modelo, color, cv):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cv = cv
        
    def describirCoche (self):
        return f"mi coche es un {self.marca} {self.modelo} de color {self.color} con {self.cv} cv"
    
    def caballos (self):
        return f"el coche tiene {self.cv}"
    
    def cambiarColor(self, color):
        self.color
        
    def cambiarInfo
    
mi_coche = Coche("Honda", "accord", "negro", 140)
mi_coche.cambiarColor("rojo")
print(mi_coche.describirCoche())





