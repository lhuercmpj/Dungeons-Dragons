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

        if habilidad > 100 or habilidad < 0 or nombre==None or clase not in ["Ranger","Guerrero","Mago"] or id==None or adicional==None:
            raise DatoInvalido("Alguno de los datos ingresados es inválido")
        
        aventurero_temp = Guerrero("Temp",id,0,0,0.0,0)

        if aventurero_temp in self.aventureros:
            raise EntidadYaExiste("El aventurero ya está registrado, la ID no es única")
        
        if clase == "Guerrero":
            if adicional<0 or adicional >100:
                raise DatoInvalido
            nuevo_aventurero = Guerrero(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)
            
        elif clase == "Mago":
            if adicional<1 or adicional >1000:
                raise DatoInvalido
            nuevo_aventurero = Mago(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)

        elif clase == "Ranger":
            if habilidad_mascota<0 or habilidad_mascota >50 or nombre_mascota == None:
                raise DatoInvalido
            nuevo_aventurero = Ranger(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)
            mascota = Ranger.crear_mascota(nombre_mascota,habilidad_mascota)
            nuevo_aventurero.mascota_obj = mascota
        
        return True
            
    def registrar_mision(self, nombre:str, rango:int, recompensa:int, completado:bool = False, tipo_mision:str = None, cantidad_minima_miembros:int = None):
        if nombre == None or rango == None or recompensa == None or completado == None:
            raise DatoInvalido("Alguno de los datos ingresado es inválido")
        
        elif 1 > rango > 5:
            raise DatoInvalido("El rango debe ser un valor entre 1 y 5")
        
        elif recompensa < 0:
            raise DatoInvalido("La recompensa a dar debe ser un valor positivo")
        
        elif tipo_mision not in ["Mision Individual", "Mision Grupal"]:
            raise DatoInvalido("El tipo de misión debe de ser individual o grupal")
            
        
        mision_temp = MisionIndividual(nombre,2,4)
        if mision_temp in self.misiones:
            raise EntidadYaExiste("La misión ya está registrada, el nombre no es único")
        
        if tipo_mision == "Mision Individual":
            mision = MisionIndividual(nombre,rango,recompensa,completado)
        elif tipo_mision == "Mision Grupal":
            if cantidad_minima_miembros < 1 or cantidad_minima_miembros == None:
                raise DatoInvalido("La cantidad mínima de miembros ingresada para la misión es inválida")
            mision = MisionGrupal(nombre, rango, recompensa, completado, cantidad_minima_miembros)
        
        self.misiones.append(mision)
        return True
        