#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import re

#Direccion IPv4
patron = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"

with open("emails.txt") as ListaEmail:
	for line in ListaEmail:
		emails = line.strip('\n')
		email = re.match(patron,emails)
		coincidencias = email.group()
		print (coincidencias)
		