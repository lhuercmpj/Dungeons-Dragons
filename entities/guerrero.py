from entities.aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, id, habilidad, exp, dinero, fuerza:int):
        super().__init__(nombre, id, habilidad, exp, dinero)
        self.__fuerza = fuerza
        self.__rango= None

    @property
    def fuerza(self):
        return self.__fuerza
    
    @property
    def rango (self):
        return self.__rango
    
    @rango.setter
    def rango (self,nr):
        self.__rango=nr

    @fuerza.setter
    def fuerza(self, fuerza):
        self.__fuerza = fuerza
        
    def __eq__(self,otro):
        if  not isinstance(otro,Aventurero):
            return False
        return self.id == otro.id


    def calcular_rango(self):

        habilidad_total = self.habilidad + (self.fuerza/2)

        if 1 <= habilidad_total <= 20:
                self.rango=1
        elif 21 <= habilidad_total <= 40:
                self.rango=2
        elif 41 <= habilidad_total <= 60:
                self.rango=3
        elif 61 <= habilidad_total <= 80:
                self.rango = 4
        else: self.rango = 5

        return
    
