"""3- Calculadora de edad: Crea un programa que solicite al usuario su fecha de nacimiento y calcule su edad en años, meses y días"""
"""4- Cronómetro: Implementa un cronómetro en Python que calcule el tiempo transcurrido entre un punto de inicio y un punto de parada, mostrando los resultados en horas, minutos y segundos"""
"""5- Calculadora de fecha futura: Pide al usuario una fecha de inicio y una duración en días, y muestra la fecha resultante después de agregar la duración a la fecha de inicio"""
"""6- Conversor de formatos de fecha: Escribe un programa que solicite al usuario una fecha en un formato específico (por ejemplo, "dd/mm/aaaa") y lo convierta a otros formatos comunes, como "mm/dd/aaaa" o aaaa-mm-dd"""
# print(range(5,15))
# melisa.frisoli@uner.edu.ar
# santiago.salinas@uner.edu.ar
# santiago.fiotto@uner.edu.ar


import datetime
def cuanto_anios_meses_dias_tengo(fecha_de_nacimiento):
    dia,mes,anio=map(int,fecha_de_nacimiento.split("/"))
    fecha_de_nacimiento=datetime.date(anio,mes,dia)
    hoy=datetime.date.today()
    anios=hoy.year - fecha_de_nacimiento.year
    meses=hoy.month - fecha_de_nacimiento.month
    dias=hoy.day - fecha_de_nacimiento.day
    if meses<0:
        anios-=1
        meses+=12
    #return anios,meses,dias
    
    print(f"Tengo {anios} años, {meses} meses y {dias} días")

cuanto_anios_meses_dias_tengo("14/10/1977")
