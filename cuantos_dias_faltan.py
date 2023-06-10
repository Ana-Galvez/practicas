from modulos_propios import cuantos_dias_faltan

def main():
    print("""BIENVENIDO:
Este pequeño programa te ayudará a calcular cuantos días faltan para alguna fecha""")

    ingreso_while=True
    while ingreso_while:
        print("¿Qué deseas hacer?")
        print("""
        1- Calcular cuantos días faltan
        2- Salir
        """)
        ingreso_opcion=int(input("Ingrese el número de la opción: "))
        if ingreso_opcion==1:
            print(f"El resultado es: {cuantos_dias_faltan()} días \n")
        elif ingreso_opcion==2:
            print("GRACIAS POR USAR ESTA APLICACIÓN")
            ingreso_while=False
            
main()