#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import re

#Direccion IPv4
patron = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

with open("IPs.txt") as IPs:
	for line in IPs:
		ips = line.strip('\n')
		ip = re.match(patron,ips)
		coincidencias = ip.group()
		print (coincidencias)
		