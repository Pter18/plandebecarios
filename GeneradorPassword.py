#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

'''
Programa que genera contraseñas seguras
'''
import sys
import string
import random

def DefaultRandomPassword(passwordCharacters, minLetters, maxLetters,x):
    passwd = "".join(random.choice(passwordCharacters) for i in range(random.randint(minLetters, maxLetters)))
    print (passwd)
    if (x < NumPasswd):
    	DefaultRandomPassword(passwordCharacters, minLetters, maxLetters,x+1)

#Numero de contraseas generadas
NumPasswd = 15
#Parametros de passwords
#Longitud de minimo de caracteres
minLetters = 8
#Longitud de maxima de caracteres
maxLetters = 16
#Alfabeto a utilizar
passwordCharacters = string.ascii_letters + string.digits + string.punctuation
x = 1

DefaultRandomPassword(passwordCharacters, minLetters, maxLetters,x)
