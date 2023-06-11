def divisores(numero:int)->list:
    lista=[]
    for i in range(1, numero+1):
        if numero % i == 0:
            lista.append(i)
    return lista

def main():
    print("""BIENVENID@
    Este pequeño programa te mostrará todos los divisores que posee el número elegido""")
    
    numero=int(input("ingresa numero: "))
    print(f"Los divisores del numero {numero} son:\n{divisores(numero)}")

main()