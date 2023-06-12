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

def que_dia_fue_o_sera(fecha:str)->str:
    """Función donde se pide una fecha y devuelve que día fue o será"""
    import datetime
    dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    dia,mes,anio=map(int,fecha.split('/'))

    fecha=datetime.date(anio,mes,dia)
    que_dia=fecha.weekday()
    que_dia_es= dias[que_dia]
    return que_dia_es

def calculadora_de_dias(fecha_comienzo:str,fecha_final:str)->int:
    """Función donde se pide 2 fechas y saca la diferencia en días"""
    import datetime
    diac,mesc,anioc= map(int,fecha_comienzo.split('/'))
    diaf,mesf,aniof= map(int,fecha_final.split('/'))

    fecha_comienzo_date=datetime.date(anioc,mesc,diac)
    fecha_final_date=datetime.date(aniof,mesf,diaf)

    resultado=fecha_final_date-fecha_comienzo_date
    dias=resultado.days
    return dias