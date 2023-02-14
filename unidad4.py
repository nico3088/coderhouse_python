""""Ejercicicos unidad 4
Descripción de la actividad.
Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado.
Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: “No existe generación asociada

1920-1945 Silenciosa

1946-1964 Baby Boomer

1965-1979 X

1980-2000 Y

2001-2010 Z """

"""generacion = int(input("Escribe tu anio de nacimiento"))

if generacion >= 1920 and generacion <= 1945 :
    print("Eres de la generacion silenciosa")
elif generacion > 1945 and generacion <= 1964:
    print("Eres de la generacion Baby Boomer")
elif generacion >= 1965 and generacion <= 1979:
    print("Eres de la generacion X ")    
elif generacion >= 1980 and generacion <= 2000:
    print("Eres de la generacion Y")
elif generacion >= 2001 and generacion <= 2010:
    print("Eres de la generacion Z")
else:
    print ("No existe generacion asociada")"""
    
"""Ej 2: Aprobación de Crédito bancario 
Descripción de la actividad.

Para aprobar un crédito, el cliente debe ser mayor de edad. Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares. En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. Si no cumple ninguna de las condiciones, no se aprueba el crédito.

Datos iniciales

edad = 15

antigüedad = 10

ingreso = 1500"""

"""edad = int(input("Ingrese su edad"))
antiguedad = int(input("Ingrese su antiguedad financiera"))
ingreso = int(input("Ingrese su sueldo"))

if edad < 18:
    print("Lo sentimos ustd no es mayor de edad")
elif ingreso < 2500:
    print("Lo sentimos no tiene los ingresos necesarios para poder solicitar el prestamo")
elif antiguedad < 3 and ingreso < 4000:
    print("Lo sentimos no tiene la antiguedad necesaria para solicitar el credito")
else: 
    print("Cumple con todos los requisitos, se le otorgara su credito")"""
    
"""Ej 2: Marvel vs Capcom 
Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a una preferencia (Marvel o Capcom).

El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre posterior a la N y el grupo B por el resto.

Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla el grupo que le corresponde"""
    
"""nombre = input("Ingrese su nombre")
preferencia = input("Ingrese si es fan de Marvel o Capcom")

if (nombre < 'M' and preferencia == 'Marvel') or (nombre >'N' and preferencia == 'Capcom'):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")"""

    
