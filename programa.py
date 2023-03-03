# programa para identificar si un numero es positivo y de cuatro digitos 

print("-----------------------------------------")
print("----NUMERO DE CUATRO DIGITOS POSITIVO----")
print("-----------------------------------------")

# Input

n = int(input("ingrese un valor: "))

# procesing

n1 = n >= 0 
n2 = 999 < n < 10000
n3 = -10000 < n < -999

#output

if (n1 == True):
    print("Es un numero positivo")
else:
   print("Es un numero negativo")

if (n2 == True)+(n3 == True):
    print ("Es un numero de cuatro dijitos")
   
else:
   print("No es un numero de cuatro digitos")

























