#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice #Impormanos una funcion de unalibreria

calificacion_alumno = {}                    #Diccionario Vacio
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)   #Conjunto o Tupla
becarios = ['Juan Manual',                  #Lista
            'Ignacio',
            'Valeria',
            'Luis Antonio',
            'Pedro Alejandro',
            'Diana Guadalupe',
            'Jorge Luis',
            'Jesika',
            'Jesús Enrique',
            'Rafael Alejandro',
            'Servando Miguel',
            'Ricardo Omar',
            'Laura Patricia',
            'Isaías Abraham',
            'Oscar']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def imprime_aprobados():
    aprobados=[]
    reprobados=[]
    for alumno in calificacion_alumno:
        if calificacion_alumno[alumno] >= 8:
            aprobados.append(alumno)
        else:
            reprobados.append(alumno)
    apro=tuple(aprobados)
    repro=tuple(reprobados)
    return apro,repro

def imprime_promedio():
    cont=0
    suma=0.0
    promedio=0.0
    for calificacion in calificacion_alumno:
        suma += calificacion_alumno[calificacion]
        cont += 1
    promedio = suma/cont
    return cont, suma, promedio

asigna_calificaciones()
#imprime_calificaciones()
print imprime_aprobados()
print imprime_promedio()
