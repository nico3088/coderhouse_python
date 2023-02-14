"""Descripción de la actividad.

En esta actividad, podrás poner en práctica todo lo aprendido durante la sesión.

Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

Añade a la LISTA1 el int 456789 y luego el string “Hola Mundo”
Luego añade a la LISTA2 el string “Hola y Adios” y luego el int 5555
Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento
Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3"""

lista_1 = [1, 2, 3, 4, 'pepe', 'hola']

lista_2 = [ 1, 5, ('mi', 'gato'),'richard']

lista_1.append(456789)
lista_1.append("Hola Mundo")

lista_2.append("Hola y Adios")
lista_2.append(5555)

lista_2[4:] = ['Hola y Adios', 55555]

print(lista_1)
print(lista_2)

lista_3 = lista_1[:-1]
"""lista_1.pop()/No es conveniente modifica el contenido de lista_1"""
print(lista_3)

lista_4 = lista_2[1:-1]
print(lista_4)

lista_5 = lista_3 + lista_4
print(lista_5)


"""Descripción de la actividad. A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

El último ítem de tupla
El número de ítems de tupla
La posición donde se encuentra el ítem 87 de tupla
Una lista con los últimos tres ítems de tupla
Un ítem que haya en la posición 8 de tupla
El número de veces que el ítem 7 aparece en tupla
Copia esta tupla para iniciar el ejercicio: tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)"""

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

print(tupla[-1])
print(len(tupla))
print(tupla.index(87))
print(tupla[-3:])
print(tupla[8])
print(tupla.count(7))


