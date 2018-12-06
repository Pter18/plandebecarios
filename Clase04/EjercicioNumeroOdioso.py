#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

'''
Un número odioso (odious number) es todo aquél 
que su representación en binario tiene un número 
impar de unos.
'''

{x: (bin(x), hex(x)) for x in range (50) if bin(x).count('1') % 2 != 0}