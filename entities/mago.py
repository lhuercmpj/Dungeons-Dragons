from entities.aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, id, habilidad, exp, dinero, mana:int):
        super().__init__(nombre, id, habilidad, exp, dinero)
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, mana):
        self.__mana = mana

    def asignar_exp(self):
        pass

    def asignar_recompensa(self):
        pass

    def calcular_rango(self):
        pass