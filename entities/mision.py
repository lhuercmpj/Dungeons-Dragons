from abc import ABC

class Mision(ABC):
    
    def __init__(self,nombre:str, rango:int, recompensa:float, completado:bool):
        self.__nombre = nombre
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado
        self.__aventureros = []
        
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def rango(self):
        return self.__rango
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def completado(self):
        return self.__completado
    
    @property
    def aventureros(self):
        return self.__aventureros
    
    @aventureros.setter
    def aventureros (self, nuevos_aventureros):
        self.__aventureros = nuevos_aventureros

    @completado.setter
    def completado (self, nuevo_estado):
        self.__completado = nuevo_estado
    
    def __eq__(self,otro):
        if  not isinstance(otro,Mision):
            return False
        return self.nombre == otro.nombre


    def repartir_recompensa(self,aventureros):
        recompensa_dividida = self.recompensa / len(aventureros)
        for aventurero in aventureros:
            aventurero.dinero += recompensa_dividida

    def repartir_exp(self,aventureros_reales):
        
        match self.rango:
            case 1: 
                puntos_exp = 5
            case 2: 
               puntos_exp = 10
            case 3: 
                puntos_exp = 20
            case 4: 
                puntos_exp = 50
            case 5: 
                puntos_exp = 100

        for aventurero in aventureros_reales:
            aventurero.exp += puntos_exp


