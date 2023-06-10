from modulos_propios import potencia
from modulos_propios import raiz

def main():
    print("""BIENVENIDO:
Este pequeño programa te ayudará a calcular cualquier potencia y/o cualquier raiz""")

    ingreso_while=True
    while ingreso_while:
        print("¿Qué deseas hacer?")
        print("""
        1- Calcular Potencia
        2- Calcular Raíz
        3- Salir
        """)
        ingreso_opcion=int(input("Ingrese el número de la opción: "))
        if ingreso_opcion==1:
            print(f"El resultado es: {potencia()} \n")
        elif ingreso_opcion==2:
            print(f"El resultado es {raiz()} \n")
        elif ingreso_opcion==3:
            print("GRACIAS POR USAR ESTA APLICACIÓN")
            ingreso_while=False

main()