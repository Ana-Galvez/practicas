def cuantas_vocales():
    vocales="aeiouáéíóú"
    oracion=input("Ingresa la oración: ")
    oracion_minuscula=oracion.lower()
    contador_de_vocales=0

    for letra in oracion_minuscula:
        if letra in vocales:
            contador_de_vocales+=1

    print(f"La cantidad de vocales que tiene tu oración: {contador_de_vocales}")

def main():
    print("""BIENVENIDO
Esta pequeña aplicación te dirá la cantidad de vocales que
tiene tu oración""")
    cuantas_vocales()

main()