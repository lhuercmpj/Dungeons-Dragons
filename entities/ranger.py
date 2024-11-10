from .mascota import Mascota
from .aventurero import Aventurero

class Ranger(Aventurero):
    def __init__(self, nombre, id, habilidad, exp, dinero):
        super().__init__(nombre, id, habilidad, exp, dinero)
        self.__mascota = None
        self.__rango = None

    @property
    def mascota(self):
        return self.__mascota
    
    @property
    def rango (self):
        return self.__rango
    
    @rango.setter
    def rango (self,nr):
        self.__rango=nr
   
    @mascota.setter
    def mascota(self,mascota_nueva):
        self.__mascota = mascota_nueva

  
    def calcular_rango(self):
        if self.mascota:
            habilidad_total= self.habilidad + self.mascota_obj.habilidad
            if 1 <= habilidad_total <= 20:
                self.rango=1
            elif 21 <= habilidad_total <= 40:
                self.rango=2
            elif 41 <= habilidad_total <= 60:
                self.rango=3
            elif 61 <= habilidad_total <= 80:
                self.rango = 4
            else: self.rango = 5
        if self.mascota == False:
            if 1 <= self.habilidad <= 20:
                self.rango=1
            elif 21 <= self.habilidad <= 40:
                self.rango=2
            elif 41 <= self.habilidad <= 60:
                self.rango=3
            elif 61 <= self.habilidad <= 80:
                self.rango = 4
            else: self.rango = 5

    
    def crear_mascota(self, nombre_mascota, habilidad_mascota):
        self.mascota = Mascota(nombre_mascota, habilidad_mascota)
        
            

