# false = 0
# true = 1
# Ejercicio 1
expresiones = [
    False == True,
    10 >= 2*4,
    33/3 == 11,
    True > False,
    True*5 == 2.5*2
]
print(expresiones)

# not invierte el valor
# Ejercicio2
expresiones_2 = [
    not False,
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23,
    12 > 7 and True < False
]
print(expresiones_2)

# Ejercicio 3
# NOMBRE sea diferente de cuatro asteriscos “****”
# EDAD sea mayor que 5 y a su vez menor que 20
# Que la longitud de NOMBRE sea mayor o igual a 4 pero a la vez menor que 8
# EDAD multiplicada por 3 sea mayor que 35

nombre = input('Ingrese un nombre')

edad = (input('Ingrese su edad'))

requisitos = nombre != '****' and 5 < edad < 20 and 4 <= len(nombre) < 8 and edad * 3 > 35

print (requisitos)