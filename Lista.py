##from colorama import Fore, Style, init

# Inicializa colorama
#init(autoreset=True)

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Borrar tarea")
    print("3. Editar tarea")
    print("4. Mostrar tareas")
    print("5. Guardar tareas en archivo")
    print("6. Salir")

def agregar_tarea(tareas, ultimo_id):
    tarea = input("Ingrese la tarea a agregar: ")

    while True:
        fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
        if fecha.replace("/", "").isdigit() and len(fecha) == 10:
            break
        else:
            print("Por favor, ingrese una fecha válida en el formato dd/mm/aaaa.")

    while True:
        hora = input("Ingrese la hora (HH:MM): ")
        if hora.replace(":", "").isdigit() and len(hora) == 5:
            break
        else:
            print("Por favor, ingrese una hora válida en el formato HH:MM.")

    estado = input("Ingrese el estado (Iniciada, en progreso, completada): ")

    ultimo_id += 1  # Incrementamos el ID para la nueva tarea
    tareas.append((ultimo_id, tarea, fecha, hora, estado))
    print(f"Tarea '{tarea}' con ID {ultimo_id} ha sido agregada.")
    return ultimo_id  # Devolvemos el nuevo último ID


def borrar_tarea(tareas):
    while True:
        try:
            id_tarea = int(input("Ingrese el ID de la tarea a borrar: "))
            break  # Sale del bucle si la conversión a entero es exitosa
        except ValueError:
            print("Por favor, ingrese un número válido como ID.")

    tarea_encontrada = False
    for tarea in tareas:
        if tarea[0] == id_tarea:
            tareas.remove(tarea)
            tarea_encontrada = True
            print(f"Tarea con ID {id_tarea} ha sido borrada.")
            break

    if not tarea_encontrada:
        print("El ID de la tarea no existe en la lista.")


def editar_tarea(tareas):
    while True:
        try:
            id_tarea = int(input("Ingrese el ID de la tarea a editar: "))
            break  # Sale del bucle si la conversión a entero es exitosa
        except ValueError:
            print("Por favor, ingrese un número válido como ID.")

    tarea_encontrada = False
    for i, tarea in enumerate(tareas):
        if tarea[0] == id_tarea:
            nueva_tarea = input("Ingrese la nueva tarea: ")

            while True:
                nueva_fecha = input("Ingrese la nueva fecha (dd/mm/aaaa): ")
                if len(nueva_fecha) == 10 and nueva_fecha[2] == nueva_fecha[5] == '/' and nueva_fecha[:2].isdigit() and nueva_fecha[3:5].isdigit() and nueva_fecha[6:].isdigit():
                    break
                else:
                    print("Por favor, ingrese una fecha válida en el formato dd/mm/aaaa.")

            while True:
                nueva_hora = input("Ingrese la nueva hora (HH:MM): ")
                if len(nueva_hora) == 5 and nueva_hora[2] == ':' and nueva_hora[:2].isdigit() and nueva_hora[3:].isdigit():
                    break
                else:
                    print("Por favor, ingrese una hora válida en el formato HH:MM.")

            nuevo_estado = input("Ingrese el nuevo estado (Iniciada, en progreso, completada): ")
            tareas[i] = (id_tarea, nueva_tarea, nueva_fecha, nueva_hora, nuevo_estado)
            print(f"Tarea con ID {id_tarea} ha sido editada.")
            return

    print("El ID de la tarea no existe en la lista.")



'''def mostrar_tareas(tareas):
    if tareas:
        print("Tareas en la lista:")
        for tarea in tareas:
            color = Fore.WHITE  # Color por defecto
            if tarea[4] == "Iniciada":
                color = Fore.BLUE
            elif tarea[4] == "En proceso":
                color = Fore.YELLOW
            elif tarea[4] == "Terminada":
                color = Fore.GREEN
            print(color + f"ID: {tarea[0]}, Tarea: {tarea[1]}, Fecha: {tarea[2]}, Hora: {tarea[3]}, Estado: {tarea[4]}")
    else:
        print("La lista está vacía.")
        '''

def mostrar_tareas(tareas):
    if tareas:
        print("{:<5} {:<20} {:<12} {:<10} {:<15}".format("ID", "Tarea", "Fecha", "Hora", "Estado"))
        print("-" * 65)  # Línea separadora

        for tarea in tareas:
            print("{:<5} {:<20} {:<12} {:<10} {:<15}".format(*tarea))
    else:
        print("La lista está vacía.")

    # Mostrar tareas desde el archivo si existe
    try:
        with open("tareas.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido:
                print("\nTareas almacenadas en 'tareas.txt':")
                print(contenido)
    except FileNotFoundError:
        pass  # Ignorar si el archivo no existe



   
        
def guardar_tareas(tareas):
    with open("tareas.txt", "w") as archivo:  # Cambio a modo "w" (write)
        for tarea in tareas:
            archivo.write(f"{tarea[0]}, {tarea[1]}, {tarea[2]}, {tarea[3]}, {tarea[4]}\n")
    print("Tareas guardadas en tareas.txt.")



def main():
    tareas = []
    ultimo_id = 0  # Inicializamos el ID de la última tarea agregada
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ultimo_id = agregar_tarea(tareas, ultimo_id)  # Actualizamos el último ID después de agregar una tarea
        elif opcion == "2":
            borrar_tarea(tareas)
        elif opcion == "3":
            editar_tarea(tareas)
        elif opcion == "4":
            mostrar_tareas(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
    
    
    