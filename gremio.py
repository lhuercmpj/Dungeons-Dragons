from entities import Aventurero,Guerrero,Mago,Mascota,Mision,MisionIndividual,MisionGrupal
from exceptions import EntidadYaExiste,EntidadNoExiste

class Gremio:
    
    def __init__(self):
        self.__aventureros = []
        self.__misiones = []
        
    @property
    def aventureros(self):
        return self.__aventureros
    
    @property
    def misiones(self):
        return self.__misiones
    
    