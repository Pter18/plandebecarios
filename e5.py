#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

eq1 = ['Juan Manuel','Ignacio','Valeria','Luis Antonio','Pedro Alejandro']
eq2 = ['Diana Guadalupe','Jorge Luis','Jesika','Jesus Enrique','Rafael Alejandro']
eq3 = ['Servando Miguel','Ricardo Omar','Laura Patricia','Isaias Abraham','Oscar']

#expresion funcional:
# 1) funcion lambda que sume las tres listas
lista=(lambda x,y,z: x+y+z)(eq1,eq2,eq3)
# 2) filtre la lista resultante para obtener a los que tienen un solo nombre (filter)
lista2=filter(lambda x:' ' not in x,lista) #Si espacio ' ' no esta en cada elemento agragara a la lista nueva.
# 3) convierta a mayusculas los nombres del resultado anterior (map)
lista3=map(lambda x: x.upper(),lista2)
# 4) obtener una cadena con los nombres resultantes, separando los nombres con coma (reduce)
reduce(lambda x,y: x + ',' + y,lista3)
#UNA SOLA EXPRESION
reduce(lambda x,y: x + ',' +y,(map(lambda x: x.upper(),(filter(lambda x:' ' not in x,((lambda x,y,z: x+y+z)(eq1,eq2,eq3)))))))