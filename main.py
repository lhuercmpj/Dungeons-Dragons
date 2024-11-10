from gremio import Gremio
from exceptions import EntidadYaExiste,EntidadNoExiste,DatoInvalido

if __name__ == "__main__":

    gremio = Gremio()
    menu = True

    while menu:
        print("-------------------------------------")
        print("Creado por: Lautaro Siri y Lihué Rocumpaj")
        print("Bienvenido al Simulador oficial de Gremio de Aventureros de Villa-UM")
        print("Seleccione una opción:")
        print("1. Registrar Aventurero")
        print("2. Registrar Misión")
        print("3. Realizar Misión")
        print("4. Otras Consultas")
        print("5. Abandonar el gremio")
        print("-------------------------------------")
        

        try:
            respuesta = int(input("Ingrese un valor entre 1 y 5 para seleccionar: "))
            if 1 > respuesta > 5:
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
                        
                        mascota = (input("El Ranger puede tener una mascota, desea adoptar una? (S/N): "))
                        if mascota.lower() == "s":
                            adicional = True
                        elif mascota.lower() == "n":
                            adicional = False
                        
                        if adicional:
                            nombre_mascota = input("Ingresa el nombre de la mascota: ")
                            habilidad_mascota = int(input("Ingresa los puntos de habilidad de la mascota (1- 50): "))
                            gremio.registrar_aventurero(nombre,clase,id,habilidad,experiencia,dinero,adicional,nombre_mascota,habilidad_mascota)
                        else:
                            gremio.registrar_aventurero(nombre,clase,id,habilidad,experiencia,dinero,adicional)            
                        
            case 2: 
                gremio.registrar_mision
            case 3: 
                gremio.realizar_mision
            case 4: 
                pass
            case 5: 
                print("Abandondando el gremio...")
                print("Se ha abandonado el gremio.")
                menu = False
