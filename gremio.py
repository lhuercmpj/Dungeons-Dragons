from entities import Aventurero,Guerrero,Mago,Mascota,Mision,MisionIndividual,MisionGrupal,Ranger
from exceptions import EntidadYaExiste,EntidadNoExiste,DatoInvalido

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
    
    
    def registrar_aventurero(self, nombre:str, clase:str , id:int, habilidad:int , experiencia:int, dinero:float, adicional, nombre_mascota = None, habilidad_mascota= None):
        clase = clase.lower()

        if habilidad > 100 or habilidad < 0 or nombre==None or clase not in ["ranger","guerrero","mago"] or id==None or adicional==None:
            raise DatoInvalido("Alguno de los datos ingresados es inválido")
        
        aventurero_temp = Guerrero("Temp",id,0,0,0.0,0)

        if aventurero_temp in self.aventureros:
            raise EntidadYaExiste("El aventurero ya está registrado, la ID no es única")
        
        if clase == "guerrero":
            if adicional<0 or adicional >100:
                raise DatoInvalido
            nuevo_aventurero = Guerrero(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)
            
        elif clase == "mago":
            if adicional<1 or adicional >1000:
                raise DatoInvalido
            nuevo_aventurero = Mago(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)

        elif clase == "ranger":
            if habilidad_mascota<0 or habilidad_mascota >50 or nombre_mascota == None:
                raise DatoInvalido
            nuevo_aventurero = Ranger(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)
            mascota = Ranger.crear_mascota(nombre_mascota,habilidad_mascota)
            nuevo_aventurero.mascota_obj = mascota