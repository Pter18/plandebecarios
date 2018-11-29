#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
from poo import Becario

#calificacion_alumno = {}
lista=[] #Creo una lista de objetos
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Juan Manual',
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
        #Creo una variable en la cual voy asignar
        #los valores donde b=nombre y choice(calificaciones) sera la calificacion
        auxiliar=Becario(b,choice(calificaciones))
        #Una vez asigano los valores los agrego a mi lista con append(auxiliar)
        lista.append(auxiliar)
        #calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    #for alumno in calificacion_alumnolista:
    for alumno in lista:
        #print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])
        
        print alumno
asigna_calificaciones()
imprime_calificaciones()
