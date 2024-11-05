from mascota import Mascota
from aventureros import Aventurero

class Ranger(Aventurero):
    def __init__(self, nombre, id, habilidad, exp, dinero, mascota=bool):
        super().__init__(nombre, id, habilidad, exp, dinero)
        self.__mascota = mascota
        self.__mascota_obj= None

    @property
    def mascota(self):
        return self.__mascota

    def asignar_exp(self):
        pass

    def asignar_recompensa(self):
        pass

    def calcular_rango(self):
        pass
    
    def crear_mascota(self, nombre_mascota, habilidad_mascota):
        if self.__mascota:
            self.__mascota_obj = Mascota(nombre_mascota, habilidad_mascota)
            
       
