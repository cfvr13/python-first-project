

def ingreso ():
    global a,b
    a=int(raw_input("Ingrese el primer numero"))
    b=int(raw_input("Ingrese el segundo numero"))

def suma():
    print ("El resultado es; ", a+b)
    raw_input()
def resta():
    print ("El resltado es; ", a-b)
    raw_input()
def multiplicacion():
    print ("El resultado es; ", a*b)
    raw_input()
def division():
    if (b==0):
        print ("No se puede dividir por cero")
        raw_input()
    else:
        print ("El resultado es: ", a/b)
        raw_input()

while (true):
    print("1 suma")
    print("2 resta")
    print("3 multiplicacion")
    print("4 division")
    opcion=int(raw_input("Ingrese la opcion"))

    if (opcion==1):
        ingreso()
        suma()
    elif (opcion==2):
        ingreso()
        resta()
    elif (opcion==3):
        ingreso()
        multiplicacion()
    elif (opcion==4):
        ingreso()
        division()
