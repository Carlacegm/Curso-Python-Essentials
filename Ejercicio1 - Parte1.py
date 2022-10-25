# -*- coding: utf-8 -*-
"""
@author: Carla Guerrero
"""

#Se utiliza print para desplegar los mensajes que se necesitan que se muestre
print("Empezando a trabajar con Phyton")
print("Realizado por: Carla Guerrero")
print("\nConsultando los tipos de valores:")
print("\nEl tipo de dato de 875 es:")
#Se utiliza dos funciones anidadas para ahorrar lineas de código, la función type para determinar el tipo de dato y la funcion print para imprimir el tipo de dato.
print(type(875))
print("\nEl tipo de dato de 4.89 es:")
print(type(4.89))
print("\nEl tipo de dato del texto:'Now is better' es:")
print(type("Now is better"))
print("\nEl tipo de dato de 1.32 es:")
print(type(1.32))
print("\n¿El valor 5 + 8i corresponde a un valor entero?")
#Se utiliza dos funciones anidadas para ahorrar lineas de código, la función isinstance para comparar valores y la funcion print para imprimir la respuesta de esta comparación.
print(isinstance(5+8j,int))
print("\n¿El valor 8.2 corresponde a un valor entero?")
print(isinstance(8.2,int))
print("\n¿El texto:'Readability counts' corresponde a un string?")
print(isinstance("Readability counts",str))