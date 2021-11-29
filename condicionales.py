
print("Calculadora")

s: Suma
r: Resta
m: Multiplicación
d: División

print ("Ingrese el primer numero")
num1=int(input("Numero 1:"))
print ("ingrese el segundo numero")
num2=int(input("Numero 2:"))


opcion=input("seleccione el tipo de operacion que desea realizar:\n\
s=Suma\n\
r=Resta\n\
m=Multiplicacion\n\
d=Divicion\n"
)
opcion=opcion.lower()
res=0
if opcion=="s":
    res=num1+num2
if opcion=="r":
    res=num1-num2
if opcion=="m":
    res=num1*num2
if opcion=="d":
    if num2!=0:
        res=num1/num2
else:
    print("el caracter ingresado no corresponde a los indicados")
    quit()

print("el resultado es:", result)