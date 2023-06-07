def palindromo():
    continuar=True
    palabra=input("Ingresa la palabra. Para salir escribe 'salir': ")
    while continuar:
        if palabra!=palabra[::-1] and palabra!="salir":
            print(f"La palabra {palabra} NO ES PALÍNDROMO")
            palabra=input("Ingresa la palabra. Para salir escribe 'salir': ")
        elif palabra==palabra[::] and palabra!="salir":
            print(f"La palabra {palabra} ES PALÍNDROMO")
            palabra=input("Ingresa la palabra. Para salir escribe 'salir': ")
        else:
            continuar=False
        
    print("GRACIAS POR JUGAR")

def main():
    print("""BIENVENIDO
Esta pequeña aplicación te dirá si la palabra ingresada es o no
un palíndromo (palabra que se puede leer de izquierda a derecha y
de derecha a izquierda)""")
    palindromo()

main()