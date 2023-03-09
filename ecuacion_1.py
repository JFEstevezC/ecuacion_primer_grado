print("-----------------------------------------")
print("---RESOLVER-LA-SIGUIENTE-ECUACION: mx+b=0") 
print("-----------------------------------------")
m= int(input("ingrese el valor de la pendiente m: "))
b= int(input("ingrese el valor del punto de intecección b: "))
if b>0:
    x=-b/m
    print("x = " +str(x))
else:
    x=b/m
    print("x = " +str(x))