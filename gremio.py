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
            nuevo_aventurero = Ranger(nombre,id,habilidad,experiencia,dinero)
            if adicional:
                if 1 > habilidad_mascota > 50  or nombre_mascota == None:
                    raise DatoInvalido("La habilidad de la mascota es inválida o vacía")
                mascota = nuevo_aventurero.crear_mascota(nombre_mascota,habilidad_mascota)
                nuevo_aventurero.mascota = mascota
            self.aventureros.append(nuevo_aventurero)
        return True
            
    
    
    def registrar_mision(self, nombre:str, rango:int, recompensa:int,tipo_mision:str = None, completado:bool = False, cantidad_minima_miembros:int = None):
        if nombre == None or rango == None or recompensa == None or completado == None:
            raise DatoInvalido("Alguno de los datos ingresado es inválido")
        
        elif 1 > rango > 5:
            raise DatoInvalido("El rango debe ser un valor entre 1 y 5")
        
        elif recompensa < 0:
            raise DatoInvalido("La recompensa a dar debe ser un valor positivo")
        
        elif tipo_mision not in ["Mision Individual", "Mision Grupal"]:
            raise DatoInvalido("El tipo de misión debe de ser individual o grupal")
            
        completado_temp=False
        mision_temp = MisionIndividual(nombre,2,3,completado_temp)
        if mision_temp in self.misiones:
            raise EntidadYaExiste("La misión ya está registrada, el nombre no es único")
        
        if tipo_mision == "Mision Individual":
            mision = MisionIndividual(nombre,rango,recompensa,completado)
            self.misiones.append(mision)
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
        aventureros_reales=[]
        for aventurero in aventureros:
            if not aventurero in self.aventureros:
                raise EntidadNoExiste ("Aventurero no registrado")
            for aventureros_posta in self.aventureros:
                if aventureros_posta == aventurero:
                    aventureros_reales.append(aventureros_posta)

                    if aventureros_posta.rango < mision.rango:
                       raise DatoInvalido ("Aventurero con rango insuficiente")

        if isinstance(mision,MisionGrupal):
            if mision.cantidad_minima_miembros > len(aventureros):
                raise DatoInvalido ("Cantidad de aventureros insuficientes")
        
        mision.completado = True
        mision.aventureros= aventureros
        mision.repartir_recompensa(aventureros_reales)
        mision.repartir_exp(aventureros_reales)
    

    def top_10_aventureros(self):                                                                  #a= elemento de la lista
        top_aventureros = sorted(self.aventureros,key=lambda a: (-a.misiones_resueltas, a.nombre)) #Sortea de mayor a menor las
                                                                                                #misiones y de menr a myr por nombre
        return top_aventureros[:10]
    
    def mostrar_top_10_aventureros(self):
        print("Top 10 Aventureros con Más Misiones Resueltas:")
        for i, aventurero in enumerate(self.top_10_aventureros(), start=1): #Start para q arranque en 1 y no 0
            print(f"{i}. {aventurero.nombre} - Misiones Resueltas: {aventurero.misiones_resueltas}")
    
    def top_5_misiones(self):
        top_misiones = sorted(self.misiones,key=lambda m: (-m.recompensa, m.nombre))#Sortea de mayor a menor las
                                                                                    #misiones y de menr a myr por nombre
        return top_misiones[:5]
    
    def mostrar_top_5_misiones(self):
        print("Top 5 Misiones con Mayor Recompensa:")
        for i, mision in enumerate(self.top_5_misiones(), start=1):
            print(f"{i}. {mision.nombre} - Recompensa: {mision.recompensa}")

    def top_10_aventureros_habilidad(self):
    
        aventureros_con_habilidad = []
    
        for aventurero in self.aventureros:
            if isinstance(aventurero, Guerrero):
                habilidad_total = aventurero.habilidad + aventurero.fuerza / 2
            elif isinstance(aventurero, Mago):
                habilidad_total = aventurero.habilidad + aventurero.mana / 10
            elif isinstance(aventurero, Ranger):
                if aventurero.mascota:
                    habilidad_total = aventurero.habilidad + aventurero.mascota.habilidad
                else:
                    habilidad_total = aventurero.habilidad
            
            aventureros_con_habilidad.append((aventurero, habilidad_total))
            
        aventureros_ordenados = sorted(aventureros_con_habilidad,key=lambda x: (-x[1], x[0].nombre))
        return aventureros_ordenados 
        #x = Elemento de la lista aventurero_con_habilidad
        #x[1] habilidad total ordenada de menor a mayor
        #x[0].nombre = nombre del aventurero ordenado alfabeticamente
    
    def mostrar_top_10_aventureros_habilidad(self):
        print("Top 10 Aventureros con Mayor Habilidad Total:")
        top_aventureros = self.top_10_aventureros_habilidad()
        for i, (aventurero, habilidad_total) in enumerate(top_aventureros, start=1):
            print(f"{i}. {aventurero.nombre} - Habilidad Total: {habilidad_total}")
    
    def clasificar_y_mostrar_aventureros(self):
   
       
        aventureros_guerreros = []
        aventureros_magos = []
        aventureros_rangers = []

   
        for aventurero in self.aventureros:
            if isinstance(aventurero, Guerrero):
                aventureros_guerreros.append(aventurero)
            elif isinstance(aventurero, Mago):
                aventureros_magos.append(aventurero)
            elif isinstance(aventurero, Ranger):
                aventureros_rangers.append(aventurero)

       
        aventureros_guerreros.sort(key=lambda a: a.nombre)
        aventureros_magos.sort(key=lambda a: a.nombre)
        aventureros_rangers.sort(key=lambda a: a.nombre)

        
        print("Aventureros de la clase Guerrero:")
        if aventureros_guerreros:
            for guerrero in aventureros_guerreros:
                print(f"  - {guerrero.nombre}")
        else:
            print("  No hay aventureros de esta clase.")
    
        print("\nAventureros de la clase Mago:")
        if aventureros_magos:
            for mago in aventureros_magos:
                print(f"  - {mago.nombre}")
        else:
            print("  No hay aventureros de esta clase.")
    
        print("\nAventureros de la clase Ranger:")
        if aventureros_rangers:
            for ranger in aventureros_rangers:
                print(f"  - {ranger.nombre}")
        else:
            print("  No hay aventureros de esta clase.")
    

        
