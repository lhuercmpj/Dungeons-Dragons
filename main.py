from gremio import Gremio
from exceptions import EntidadYaExiste,EntidadNoExiste,DatoInvalido
from entities import MisionIndividual,MisionGrupal,Aventurero,Guerrero,Mago,Ranger
if __name__ == "__main__":

    gremio = Gremio()
    menu = True
        
    print("Creado por: Lautaro Siri y Lihué Rocumpaj")
    print("Bienvenido al Simulador oficial de Gremio de Aventureros de Villa-UM")
    while menu:
        print("-------------------------------------")
        print("Seleccione una opción:")
        print("1. Registrar Aventurero")
        print("2. Registrar Misión")
        print("3. Realizar Misión")
        print("4. Otras Consultas")
        print("5. Abandonar el gremio")
        print("-------------------------------------")
        

        try:
            respuesta = int(input("Ingrese un valor entre 1 y 5 para seleccionar: "))
            if respuesta < 1 or respuesta > 5:
                raise DatoInvalido("El valor ingresado en el menú es debe de estar entre 1 y 5")
        except DatoInvalido as e:
            print(f"se ha ingresado un dato inválido: {e}")
            
        
        match respuesta:
            case 1: 
                print("Elija la clase del aventurero (Guerrero, Mago, Ranger): ")
                print("1. Guerrero")
                print("2. Mago")
                print("3. Ranger")
                clase = int(input())
                
                nombre = input("Ingrese el nombre del aventurero: ")
                id = int(input("Ingrese el ID del aventurero: "))
                habilidad = int(input("Ingrese los puntos de habilidad del aventurero (1-100): "))
                experiencia = int(input("Ingrese los puntos de experiencia del aventurero: "))
                dinero = float(input("Ingrese el dinero del aventurero: "))
                
                match clase:
                    case 1:
                        clase = "Guerrero"
                        adicional = int(input("El Guerrero tiene puntos de fuerza, ingrese los puntos de esta habilidad (1-100): "))
                        gremio.registrar_aventurero(nombre,clase,id,habilidad,experiencia,dinero,adicional)
                    case 2:
                        clase = "Mago"
                        adicional = int(input("El mago tiene puntos de maná, ingrese los puntos de esta habilidad (1-1000): "))
                        gremio.registrar_aventurero(nombre,clase,id,habilidad,experiencia,dinero,adicional)
                    case 3:
                        clase = "Ranger"
                        adicional = None
                        
                        mascota = (input("El Ranger puede tener una mascota, desea adoptar una? (S/N): ")).lower()
                        if mascota == "s":
                            adicional = True
                        elif mascota == "n":
                            adicional = False
                        else:
                            raise DatoInvalido("Se debe de ingresar S para afirmar, o N para denegar")
                        
                        if adicional:
                            nombre_mascota = input("Ingresa el nombre de la mascota: ")
                            habilidad_mascota = int(input("Ingresa los puntos de habilidad de la mascota (1- 50): "))
                            gremio.registrar_aventurero(nombre,clase,id,habilidad,experiencia,dinero,adicional,nombre_mascota,habilidad_mascota)
                        else:
                            gremio.registrar_aventurero(nombre,clase,id,habilidad,experiencia,dinero,adicional)            
                        
            case 2: 
                nombre = input("Ingrese el nombre de la misión: ")
                rango = int(input("Ingrese el rango de la misión: "))
                recompensa = float(input("Ingrese la recompensa de la misión: "))
                grupal_o_indv = input("La misión es grupal?  (S/N): ").lower()
                
                if grupal_o_indv == "s":
                    cantidad_minima = int(input("Ingrese la cantidad mínimo de participantes de la misión : "))
                    tipo_mision= "Mision Grupal"
                    gremio.registrar_mision(nombre, rango, recompensa, tipo_mision,False, cantidad_minima)
                elif grupal_o_indv == "n":
                    tipo_mision= "Mision Individual"
                    gremio.registrar_mision(nombre, rango, recompensa,tipo_mision,False)
            case 3: 
                aventureros = []
                registrar = True
                
                nombre_mision = input("Ingrese el nombre de la misión que quiera realizar: ")
                id_aventurero = int(input("Ingrese el ID del aventurero que realizará la misión: "))
                aventurero_temp = Guerrero("default",id_aventurero,1,1,1,1)
                aventureros.append(aventurero_temp)
                while registrar:
                    agregar_miembro = input("¿Registrar otro aventurero? (S/N) : ")
                        
                    if agregar_miembro == 's':
                        id_aventurero = int(input("Ingrese el ID del aventurero: "))
                        aventurero_temp = Guerrero("default",id_aventurero,1,1,1,1)
                        aventureros.append(aventurero_temp)
                            
                    elif agregar_miembro == "n":
                        registrar = False
                        
                    else:
                        raise DatoInvalido("Se debe de ingresar S para afirmar, o N para denegar")
                gremio.realizar_mision(nombre_mision,aventureros)          
            case 4: 
                consultas= True
                while consultas:
                    print("1. Ver top 10 Aventureros con mas misiones resueltas")
                    print("2. Ver top 10 Aventureros con mayor habilidad")
                    print("3. Ver top 5 Misiones con mayor recompensa")
                    print("4. Volver al Menú principal")
                    consulta= int(input())
                    match consulta:
                        case 1:
                            gremio.mostrar_top_10_aventureros()
                        case 2:
                            gremio.mostrar_top_10_aventureros_habilidad()
                        case 3:
                            gremio.mostrar_top_5_misiones()
                        case 4:
                            consultas = False
            case 5: 
                print("Abandondando el gremio...")
                print("Se ha abandonado el gremio.")
                menu = False
