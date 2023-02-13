""" 
En nuestro trabajo, nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo. Para ello, debemos considerar tres aspectos:
jugaron 20 partidos durante el torneo, los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos, el promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos
La cantidad de partidos que debemos considerar a un equipo para el ejemplo se detallan a continuación:
partidos_ganados 8 partido_empatados 7 partido_perdidos 5
Importante: Cada una de las cantidades de partidos ganados, empatados o perdidos debe solicitarse al usuario utilizando la función input().
Deslogueo de github 
"""

"""Primer_desafio_unidad_1"""

cantidad_de_partidos = 20
puntaje_partidos_ganados = 3
puntaje_partidos_empatados = 1
puntaje_partidos_perdidos = 0

partidos_ganados = int(input('Cantidad de partidos ganados'))
partidos_empatdos = int(input('Cantidad de partidos empatados'))
partidos_perdidos = int(input('Cantidad de partidos perdidos'))

puntaje_total =(puntaje_partidos_ganados * partidos_ganados) + (puntaje_partidos_empatados * partidos_empatdos) + (puntaje_partidos_perdidos
*partidos_perdidos)
promedio_equipo = puntaje_total / cantidad_de_partidos
print (promedio_equipo)

"""Segundo_desafio_unidad_1
Dadas cuatro variables con diferentes textos (de forma individual), genera una nueva variable con el siguiente contenido:

Objetivo: “Python es un lenguaje de programación versátil” """

cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"

print (cadena_2, cadena_3, cadena_4, cadena_1)

