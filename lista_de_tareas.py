"""Este programa agrega, elimina y muestra una lista de tareas"""
lista_de_tareas=[]

def agregar_tareas()->list:
    agregar=input("¿Que tarea/s deseas agregar?:  ")
    agregar_formateado=agregar.capitalize()
    lista_de_tareas.append(agregar_formateado)
    return lista_de_tareas

def eliminar_tareas()->list:
    eliminar=int(input("¿Cuál tarea deseas eliminar (Presiona el número que le corresponda?: "))
    
    if len(lista_de_tareas)!=1:
        lista_de_tareas.pop(eliminar-1)
        return lista_de_tareas
    else:
        lista_de_tareas.clear()
        return lista_de_tareas

def ver_tareas():
    print("----------- LISTA DE TAREAS -----------")

    if len(lista_de_tareas)!=0:
        for indice,elemento in enumerate (lista_de_tareas):
            print(f"{indice+1}: {elemento}")
        print("")
    else:
        print("LISTA VACÍA\n")

def main():
    print("""
BIENVENIDO: Este pequeño programa te permite agregar, eliminar y ver las tareas que desees
    """)
    
    inicio_while=True
    while inicio_while or ingreso!=4:
        print("¿Qué deseas hacer?")
        print("""
        1- Agregar una tarea
        2- Ver tareas
        3- Eliminar tarea
        4- Salir
        """)
        ingreso=int(input("Ingrese el número de la opción elegida: "))
        if ingreso==1:
            agregar_tareas()
        elif ingreso==2:
            ver_tareas()
        elif ingreso==3:
            eliminar_tareas()
        elif ingreso==4:
            print("GRACIAS POR USAR LA APLICACIÓN")
            inicio_while=False
    
main()