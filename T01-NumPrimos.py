#!/usr/bin/python
# -*- coding: utf-8 -*-

user_input = input("Introduce el número a evaluar: ")

if type(user_input) == int:
    print(str(user_input) + " es un entero")
    if (user_input % 2) == 0:
        print("El número " + str(user_input) + " no es primo.")
    else:
        print("El número " + str(user_input) + " es primo.")
if type(user_input) == str:
    print(str(user_input) + " no es un entero, es un String")