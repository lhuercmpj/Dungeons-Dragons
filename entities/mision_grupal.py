from .mision import Mision

class MisionGrupal(Mision):
    
    def __init__(self,nombre:str, id:int, recompensa:float, completado:bool, cantidad_minima_miembros:int):
        super().__init__(self, nombre, id, recompensa, completado)
        self.__cantidad_minima_miembros = cantidad_minima_miembros
        
    @property
    def cantidad_minima_miembros(self):
        return self.__cantidad_minima_miembros