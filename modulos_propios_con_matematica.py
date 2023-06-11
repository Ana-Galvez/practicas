def potencia ()->float:
    """Función que el usuario agrega la base y la potencia y devuelve el resultado"""
    from math import pow
    agregar_base=int(input("Ingresa el número que será la base: "))
    agregar_potencia=int(input("Ingresa el número que será la potencia: "))
    resultado=pow(agregar_base,agregar_potencia)
    return resultado 

def raiz ()->float:
    """Función para sacar la raiz de cualquier número pedido por el usuario"""
    from math import pow
    agregar_radicando=int(input("Ingresa el número como radicando: "))
    agregar_indice=int(input("Ingresa el número como índice: "))
    resultado=pow(agregar_radicando,(1/agregar_indice))
    return resultado