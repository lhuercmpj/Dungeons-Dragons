class Mascota:
    def __init__(self, nombre, habilidad):
        self.__nombre = nombre
        self.__habilidad = habilidad

    @property
    def nombre(self):
        return self.__nombre
    @property
    def habilidad(self):
        return self.__habilidad