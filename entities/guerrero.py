from aventureros import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, id, habilidad, exp, dinero, fuerza):
        super().__init__(nombre, id, habilidad, exp, dinero)
        self.__fuerza = fuerza

    @property
    def fuerza(self):
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, fuerza):
        self.__fuerza = fuerza

    def asignar_exp(self):
        pass

    def asignar_recompensa(self):
        pass

    def calcular_rango(self):
        pass