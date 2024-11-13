from abc import ABC, abstractmethod

class Aventurero(ABC):
    def __init__(self, nombre:str, id:int, habilidad:int, exp:int, dinero:float) -> None:
        self.__nombre = nombre
        self.__id = id
        self.__habilidad = habilidad
        self.__exp = exp
        self.__dinero = dinero
        self.__misiones_resueltas = 0


    @property
    def nombre(self):
        return self.__nombre


    @property
    def id(self):
        return self.__id

  
    @property
    def habilidad(self):
        return self.__habilidad

   
    @property
    def exp(self):
        return self.__exp

    
    @property
    def dinero(self):
        return self.__dinero

        
    @property
    def misiones_resueltas(self):
        return self.__misiones_resueltas
    
    @exp.setter
    def exp(self, exp):
        self.__exp = exp

    @dinero.setter
    def dinero(self, dinero):
        self.__dinero = dinero
        
    @misiones_resueltas.setter
    def misiones_resueltas(self, nuevo_valor):
        self.__misiones_resueltas += nuevo_valor
    
    def __eq__(self,otro):
        if  not isinstance(otro,Aventurero):
            return False
        return self.id == otro.id


    @abstractmethod
    def calcular_rango(self):
        pass