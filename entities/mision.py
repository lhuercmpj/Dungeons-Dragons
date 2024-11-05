from abc import ABC

class Mision(ABC):
    
    def __init__(self,nombre:str, id:int, recompensa:float, completado:bool):
        self.__nombre = nombre
        self.__id = id
        self.__recompensa = recompensa
        self.__completado = completado
        self.__aventureros = []
        
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def id(self):
        return self.__id
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def completa(self):
        return self.__completado
    
    @property
    def aventureros(self):
        return self.__aventureros
    
    
    
    
    