#!/usr/bin/python
# -*- coding: utf-8 -*-
primos = []

def esPrimo(n,x):
	'''
	Funcion que verifica si es un numero primo obtenendo el modulo del mismo,
	esta se vuelve a llamar las veces necesarias hasta cumplir el numero de 
	numeros que se desa obtener
	'''
	if (x%2)!=0:
		primos.append(x)
	if (len(primos))!=n:	
		esPrimo(n,x+1)

#Cantidad de numeros primos que se desea calcular
user_input = "hola"	
x=1
if type(user_input) == int:
	esPrimo(user_input,x)
	print (primos[::])
else:
	print ("No estoy haciendo nada, por no soy un numero entero")
#print 






