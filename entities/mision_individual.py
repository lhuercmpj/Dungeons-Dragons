from .mision import Mision

class MisionIndividual(Mision):
    
    def __init__(self,nombre:str, id:int, recompensa:float, completado:bool):
        super().__init__(self, nombre, id, recompensa, completado)