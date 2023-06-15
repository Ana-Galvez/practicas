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
    4- Días vividos hasta hoy
    5- Salir
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
            fecha_de_nacimiento=input("Ingresa la fecha como dia/mes/año: ")
            cuantos_dias_hasta_hoy=modulos_propios_con_fechas.dias_hasta_hoy(fecha_de_nacimiento)
            print(f"Desde que nací hasta hoy, pasaron {cuantos_dias_hasta_hoy} dias\n ----------------")
        elif opcion==5:
            ingreso_while=False

main()