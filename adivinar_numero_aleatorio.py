import random as rd

print("""BIENVENIDO
Este pequeño programa crea un número aleatorio y te dará pistas
¿Podrás adivinarlo? El número está entre 1 y 100""")

numero_aleatorio=rd.randint(1,100)
ingresa_numero=int(input("Ingresa un número: "))
contador_de_intentos=0

while numero_aleatorio!=ingresa_numero:
    if numero_aleatorio<ingresa_numero:
        print("El número aleatorio es MENOR al que pusiste")
        ingresa_numero=int(input("Ingresa un número: "))
    elif numero_aleatorio>ingresa_numero:
        print("El número aleatorio es MAYOR al que pusiste")
        ingresa_numero=int(input("Ingresa un número: "))
    contador_de_intentos+=1
print(f"FELICIDADES!!! adivinaste el número al {contador_de_intentos} intento")