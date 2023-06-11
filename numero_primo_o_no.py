def primo_o_no(numero:int)->str:
    for n in range(2, numero):
        if numero % n == 0:
            return f"El numero {numero} NO ES PRIMO"
    return f"El número {numero} es primo"
    
    
def main():
    print("""BIENVENID@S
    Esta pequeña aplicación te dirá si el número elegido es o no un número primo""")
    numero=int(input("Ingrese el número: "))
    print(primo_o_no(numero))

main()