
# Numeros! 
# Escribir un programa que le pregunte al usuario números hasta que ingrese el 0,
# cuando lo haga mostrar por pantalla la suma de todos los números ingresados.

numero_Ingresado = 1
suma = 0
while numero_Ingresado != 0:
    numero_Ingresado = int(input("Ingrese un numero a sumar"))
    suma += numero_Ingresado

print("La suma dio como resultado:  " + str(suma))


"""Ejercicio 2

Haremos el siguiente listado de ejercicios:
1. Escribir un programa que enumere los países de la siguiente lista:"""
paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']

for indice, pais in enumerate(paises):
    print(f'{indice + 1}. {pais}')

"""2. Crear un bucle que sume los pares del 0 al 100"""
suma = 0 
for numero in range(101):
    suma += numero
     
print('La suma da:', suma)