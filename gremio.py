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
    
    
    def registrar_aventurero(self, nombre:str, clase:str , id:int, habilidad:int , experiencia:int, dinero:float, adicional, nombre_mascota:str = None, habilidad_mascota:int = None):

        if nombre == None or clase == None or id == None or habilidad == None or experiencia == None or dinero == None or adicional == None:
            raise DatoInvalido("Alguno de los datos ingresados es inválido")
        
        if 1 > habilidad > 100:
            raise DatoInvalido("los puntos de habilidad deben de estar entre 1 y 100")
        
        if clase not in ["Ranger","Guerrero","Mago"]:
            raise DatoInvalido("La clase seleccionada debe ser Guerrero, Mago o Ranger")
        

        aventurero_temp = Guerrero("Temp", id, 0, 0, 0.0, 0)

        if aventurero_temp in self.aventureros:
            raise EntidadYaExiste("El aventurero ya está registrado, la ID no es única")
        
        if clase == "Guerrero":
            if 1 > adicional > 100:
                raise DatoInvalido("La habilidad del guerrero es inválida")
            nuevo_aventurero = Guerrero(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)
            
        elif clase == "Mago":
            if 1 > adicional > 1000:
                raise DatoInvalido("La habilidad del mago es inválida")
            nuevo_aventurero = Mago(nombre,id,habilidad,experiencia,dinero,adicional)
            self.aventureros.append(nuevo_aventurero)

        elif clase == "Ranger":
            if adicional not in [True,False]:
                raise DatoInvalido("El dato adicional de Ranger debe ser True o False (S o N)")
            nuevo_aventurero = Ranger(nombre,id,habilidad,experiencia,dinero,adicional)
            if adicional:
                if 1 > habilidad_mascota > 50  or nombre_mascota == None:
                    raise DatoInvalido("La habilidad de la mascota es inválida o vacía")
                mascota = Ranger.crear_mascota(nombre_mascota,habilidad_mascota)
                nuevo_aventurero.mascota_obj = mascota
            self.aventureros.append(nuevo_aventurero)
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
    
    def realizar_mision(self,nombre_mision:int,aventureros:list):
        
        if nombre_mision==None or aventureros==None:
            raise DatoInvalido ("Nombre o aventureros no ingresados")

        mision_temp=MisionIndividual(nombre_mision,0,0.0,False)
        if mision_temp not in self.misiones:
            raise EntidadNoExiste ("Mision no registrada")
        
        mision = self.misiones[self.misiones.index(mision_temp)]
        
        for aventurero in aventureros:
            if aventurero not in self.aventureros:
                raise EntidadNoExiste ("Aventurero no registrado")
            if aventurero.rango < mision.rango:
                raise DatoInvalido ("Aventurero con rango insuficiente")

        if isinstance(mision,MisionGrupal):
            if mision.cantidad_minima_miembros > len(aventureros):
                raise DatoInvalido ("Cantidad de aventureros insuficientes")
        
        mision.completa = True
        mision.aventureros= aventureros
        mision.repartir_recompensa()
        mision.repartir_exp()
        

            

            
        
        

        
