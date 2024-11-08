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
    def completa(self):
        return self.__completado
    
    @property
    def aventureros(self):
        return self.__aventureros
    
    @aventureros.setter
    def aventureros (self,na):
        self.aventureros = na

    @completa.setter
    def completa (self,ne):
        self.completa=ne
    
    def __eq__(self,otro):
        if  not isinstance(otro,Mision):
            return False
        return self.nombre == otro.nombre



    def repartir_recompensa(self):
        recompensa_dividida = self.recompensa / len(self.aventureros)
        for aventurero in self.aventureros:
            aventurero.dinero += recompensa_dividida

    def repartir_exp(self):
        
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

        for aventurero in self.aventureros:
            aventurero.exp += puntos_exp


