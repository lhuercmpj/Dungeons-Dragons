from abc import ABC, abstractmethod

class Aventurero(ABC):
    def __init__(self, nombre:str, id:int, habilidad:int, exp:int, dinero:float) -> None:
        self.__nombre = nombre
        self.__id = id
        self.__habilidad = habilidad
        self.__exp = exp
        self.__dinero = dinero
        self.__misiones = []


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

  
    @property
    def habilidad(self):
        return self.__habilidad

    @habilidad.setter
    def habilidad(self, habilidad):
        self.__habilidad = habilidad

   
    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        self.__exp = exp

    
    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, dinero):
        self.__dinero = dinero
        
    @property
    def misiones(self):
        return self.__misiones
    
    def __eq__(self,otro):
        if  not isinstance(otro,Aventurero):
            return False
        return self.id == otro.id

    @abstractmethod
    def asignar_exp(self):
        pass

    @abstractmethod
    def asignar_recompensa(self):
        pass

    @abstractmethod
    def calcular_rango(self):
        pass