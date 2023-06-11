def cuantos_dias_faltan()->int:
    """Función donde el usuario pone mes y día y devuelve los días que faltan"""
    import datetime
    mes=int(input("Ingresa el mes de tu nacimiento: "))
    dia=int(input("Ingresa el día de tu nacimiento: "))

    hoy=datetime.date.today()
    fecha=datetime.date(hoy.year,mes,dia)

    if fecha<hoy:
        fecha=fecha.replace(year=hoy.year+1)
    tiempo_que_falta=fecha-hoy
    tiempo_que_falta_en_dias=tiempo_que_falta.days
    return tiempo_que_falta_en_dias

def que_dia_fue_o_sera()->str:
    """Función donde el usuario pone una fecha y devuelve que día fue o será"""
    import datetime
    dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    anio=int(input("Ingresa el año: "))
    mes=int(input("Ingresa el mes: "))
    dia=int(input("Ingresa el día: "))

    fecha=datetime.date(anio,mes,dia)
    que_dia=fecha.weekday()
    que_dia_es= dias[que_dia]
    return que_dia_es