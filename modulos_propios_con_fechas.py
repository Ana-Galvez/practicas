def cuantos_dias_faltan(mes:int,dia:int)->int:
    """Función donde se pide mes y día y devuelve los días que faltan"""
    import datetime
    
    hoy=datetime.date.today()
    fecha=datetime.date(hoy.year,mes,dia)

    if fecha<hoy:
        fecha=fecha.replace(year=hoy.year+1)
    tiempo_que_falta=fecha-hoy
    tiempo_que_falta_en_dias=tiempo_que_falta.days
    return tiempo_que_falta_en_dias

def que_dia_fue_o_sera(fecha)->str:
    """Función donde se pide una fecha y devuelve que día fue o será"""
    import datetime
    dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    dia,mes,anio=map(int,fecha.split('/'))

    fecha=datetime.date(anio,mes,dia)
    que_dia=fecha.weekday()
    que_dia_es= dias[que_dia]
    return que_dia_es

def calculadora_de_dias(fecha_comienzo,fecha_final)->int:
    """Función donde se pide 2 fechas y saca la diferencia en días"""
    import datetime
    diac,mesc,anioc= map(int,fecha_comienzo.split('/'))
    diaf,mesf,aniof= map(int,fecha_final.split('/'))

    fecha_comienzo_date=datetime.date(anioc,mesc,diac)
    fecha_final_date=datetime.date(aniof,mesf,diaf)

    resultado=fecha_final_date-fecha_comienzo_date
    dias=resultado.days
    return dias

def dias_hasta_hoy(fecha_de_nacimiento):
    import datetime
    dia_nac,mes_nac,anio_nac=map(int,fecha_de_nacimiento.split('/'))
    fecha_de_nacimiento=datetime.date(anio_nac,mes_nac,dia_nac)
    hoy=datetime.date.today()
    dias_vividos_hasta_hoy=hoy-fecha_de_nacimiento
    return dias_vividos_hasta_hoy.days

def cuanto_anios_meses_dias_tengo(fecha_de_nacimiento):
    import datetime
    dia,mes,anio=map(int,fecha_de_nacimiento.split("/"))
    fecha_de_nacimiento=datetime.date(anio,mes,dia)
    hoy=datetime.date.today()
    anios=hoy.year - fecha_de_nacimiento.year
    meses=hoy.month - fecha_de_nacimiento.month
    dias=hoy.day - fecha_de_nacimiento.day
    return anios,meses,dias