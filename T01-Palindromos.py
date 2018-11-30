#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def esPalindromo(string):
	palabras=string.split()
#	print palabras
	for palabra in palabras:
		if (palabra==palabra[::-1]):
			palindromos.append(palabra)


palindromos=[]

#esPalindromo('aza oossoo hola aeiouoiea')
esPalindromo('oso aranara sometemos reconocer aibofobia oro anna panama')
print(palindromos[::])
print(max(palindromos))