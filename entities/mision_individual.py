from .mision import Mision

class MisionIndividual(Mision):
    
    def __init__(self,nombre:str, rango:int, recompensa:float, completado:bool):
        super().__init__(nombre, rango, recompensa, completado)
        
    def __eq__(self,otro):
        if  not isinstance(otro,Mision):
            return False
        return self.nombre == otro.nombre