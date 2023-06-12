"""2- Días vividos: Pide al usuario su fecha de nacimiento y muestra cuántos días ha vivido hasta la fecha actual"""
"""3- Calculadora de edad: Crea un programa que solicite al usuario su fecha de nacimiento y calcule su edad en años, meses y días"""
"""4- Cronómetro: Implementa un cronómetro en Python que calcule el tiempo transcurrido entre un punto de inicio y un punto de parada, mostrando los resultados en horas, minutos y segundos"""
"""5- Calculadora de fecha futura: Pide al usuario una fecha de inicio y una duración en días, y muestra la fecha resultante después de agregar la duración a la fecha de inicio"""
"""6- Conversor de formatos de fecha: Escribe un programa que solicite al usuario una fecha en un formato específico (por ejemplo, "dd/mm/aaaa") y lo convierta a otros formatos comunes, como "mm/dd/aaaa" o aaaa-mm-dd"""


import modulos_propios_con_fechas

def main():
    """Proyectos con fechas"""
    print("""BIENVENID@: Este programa te servirá si quieres trabajar con fechas \n""")
    
    ingreso_while=True
    while ingreso_while:
        print("""¿Que quieres hacer?
    1- Saber cuántos días faltan
    2- Qué día fue o será
    3- Calcular cuantos días entre 2 fechas
    4- Salir
    """)
        opcion=int(input("Elije la opción con el número correspondiente: "))
        if opcion==1:
            mes=int(input("Ingresa el mes de tu nacimiento: "))
            dia=int(input("Ingresa el día de tu nacimiento: "))
            dias_que_faltan=modulos_propios_con_fechas.cuantos_dias_faltan(mes,dia)
            print(f"Faltan {dias_que_faltan} días\n -------------")
        elif opcion==2:
            fecha=input("Ingresa la fecha como dia/mes/año: ")
            que_dia=modulos_propios_con_fechas.que_dia_fue_o_sera(fecha)
            print(f"Ese día cayó {que_dia}\n ----------------")
        elif opcion==3:
            fecha_inicio=input("Ingresa la fecha más lejana como dia/mes/año: ")
            fecha_final=input("Ingresa la fecha más cercana como dia/mes/año: ")
            saber_dias=modulos_propios_con_fechas.calculadora_de_dias(fecha_inicio,fecha_final)
            print(f"Pasaron {saber_dias} días\n ----------------")
        elif opcion==4:
            ingreso_while=False

main()