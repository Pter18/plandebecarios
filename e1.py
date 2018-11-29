#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []

def aprueba_becario(nombre_completo):
    nombre_minuscula = nombre_completo.lower()
    nombre_separado = nombre_minuscula.split()
    for n in nombre_separado:
        if n in ['manuel', 'valeria', 'alejandro', 'luis', 'enrique','omar','abraham','oscar']:
            return False
    nombre_mayuscula = nombre_completo.upper()
    aprobados.append(nombre_mayuscula)
    aprobados.sort()
    return True

def elimina_becario(nombre_completo):
    nombre_mayuscula = nombre_completo.upper()
    if nombre_mayuscula in aprobados:
        aprobados.remove(nombre_mayuscula)
        print "True"
    else:
        print "False"

becarios = ['Cervantes Varela JUAN MaNuEl',
            'Leal González IgnaciO',
            'Ortiz Velarde valeria',
            'Martínez Salazar LUIS ANTONIO',
            'Rodríguez Gallardo pedro alejandro',
            'Tadeo Guillén DiAnA GuAdAlUpE',
            'Ferrusca Ortiz jorge luis',
            'Juárez Méndez JeSiKa',
            'Pacheco Franco jesus ENRIQUE',
            'Vallejo Fernández RAFAEL alejanDrO',
            'López Fernández serVANDO MIGuel',
            'Hernández González ricaRDO OMAr',
            'Acevedo Gómez LAura patrICIA',
            'Manzano Cruz isaías AbrahaM',
            'Espinosa Curiel OscaR']
for b in becarios:
    if aprueba_becario(b):
        print 'APROBADOO: ' + b
    else:
        print 'REPROBADO: ' + b

elimina_becario("Leal González IgnaciO")



#print becarios
