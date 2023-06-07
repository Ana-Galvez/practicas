import random as rd

def num_aleatorio():
    numero_aleatorio=rd.randint(1,100)
    numero=int(input("Ingresa un número: "))
    contador_de_intentos=0

    while numero_aleatorio!=numero:
        if numero_aleatorio<numero:
            print("El número aleatorio es MENOR al que pusiste")
            numero=int(input("Ingresa un número: "))
        elif numero_aleatorio>numero:
            print("El número aleatorio es MAYOR al que pusiste")
            numero=int(input("Ingresa un número: "))
        contador_de_intentos+=1
    print(f"FELICIDADES!!! adivinaste el número al {contador_de_intentos} intento")

def main():
    print("""BIENVENIDO
Este pequeño programa crea un número aleatorio y te dará pistas
¿Podrás adivinarlo? El número está entre 1 y 100""")
    num_aleatorio()

main()