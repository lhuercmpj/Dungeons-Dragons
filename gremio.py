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

        if nombre is None or clase is None or id is None or habilidad is None or experiencia is None or dinero is None or adicional is None:
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
        print(f"Aventurero {nuevo_aventurero.nombre} registrado, su id: {nuevo_aventurero.id}")
        print("Lista actual de aventureros: ")
        print(self.aventureros)
        return True
            
    
    
    def registrar_mision(self, nombre:str, rango:int, recompensa:int,tipo_mision:str = None, completado:bool = False, cantidad_minima_miembros:int = None):
        if nombre is None or rango is None or recompensa is None or completado is None:
            raise DatoInvalido("Alguno de los datos ingresado es inválido")
        
        elif 1 > rango > 5:
            raise DatoInvalido("El rango debe ser un valor entre 1 y 5")
        
        elif recompensa < 0:
            raise DatoInvalido("La recompensa a dar debe ser un valor positivo")
        
        elif tipo_mision not in ["Mision Individual", "Mision Grupal"]:
            raise DatoInvalido("El tipo de misión debe de ser individual o grupal")
            

        mision_temp = MisionIndividual(nombre,2,3,False)
        if mision_temp in self.misiones:
            raise EntidadYaExiste("La misión ya está registrada, el nombre no es único")
        
        if tipo_mision == "Mision Individual":
            mision = MisionIndividual(nombre,rango,recompensa,completado)
            self.misiones.append(mision)
        elif tipo_mision == "Mision Grupal":
            if cantidad_minima_miembros < 1 or cantidad_minima_miembros is None:
                raise DatoInvalido("La cantidad mínima de miembros ingresada para la misión es inválida")
            mision = MisionGrupal(nombre, rango, recompensa, completado, cantidad_minima_miembros)
            self.misiones.append(mision)
        return True
    
    def realizar_mision(self,nombre_mision:int,aventureros:list):
        
        if nombre_mision is None or aventureros is None:
            raise DatoInvalido ("Nombre o aventureros no ingresados")

        mision_temp = MisionIndividual(nombre_mision,1,1,False)
        if mision_temp not in self.misiones:
            raise EntidadNoExiste ("Mision no registrada")
        
        mision = self.misiones[self.misiones.index(mision_temp)]
        aventureros_mision= []
        
        for aventurero_temp in aventureros:
            if aventurero_temp not in self.aventureros:
                raise EntidadNoExiste("Alguna ID proporcionada no corresponde a ningún aventurero")
            aventurero = self.aventureros[self.aventureros.index(aventurero_temp)]
            aventureros_mision.append(aventurero)
            

        if isinstance(mision,MisionGrupal):
            if mision.cantidad_minima_miembros > len(aventureros):
                raise DatoInvalido ("Cantidad de aventureros insuficientes")
        elif isinstance(mision,MisionIndividual):
            if len(aventureros) != 1:
                raise DatoInvalido("Se agregaron varios miembros a una misión individual")
            
        
        mision.completado = True
        mision.aventureros = aventureros_mision
        mision.repartir_recompensa(aventureros_mision)
        mision.repartir_exp(aventureros_mision)
    

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
    


        
