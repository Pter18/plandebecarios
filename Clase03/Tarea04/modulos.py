#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#XML - parser
'''
Programa que parsea un archivo xml de nmap, del cual se extraera la información
necesaria en los formatos pedidos.

Modo de ejecución:
python modulos.py nmap.xml reporte.txt

Se creara un archivo llamado reporte.csv

'''
import sys
import csv
import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib

equipos = []
c_ssh = 0
c_dns = 0
c_http = 0
c_https = 0
c_up = 0
c_down = 0
n_name = 0
#Prod_http
apache = 0
nginx = 0
dianaea = 0
otros_http = 0

class Hosts:
    def __init__(self,status,ip,hostname,honeypot,ssh):      
        self.status = status
        self.ip = ip
        self.hostname = hostname
        self.honeypot = honeypot
        self.ssh = ssh
        

    def __str__(self):
        return '%s,%s,%s,%s,%s\n' % (self.status,
                                     self.ip,
                                     self.hostname,
                                     self.honeypot,
                                     self.ssh)

#Funcion MD5 para archivo nmap.xml
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    print 'MD5 DE: %s %s' % (fname, hash_md5.hexdigest())
    #return hash_md5.hexdigest()

#Funcion SHA1 para archivo nmap.xml
def sha1(fname):
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    print 'SHA1 DE: %s %s' % (fname, hash_sha1.hexdigest())
    #return hash_sha1.hexdigest()

def printError(msg, exit = False):
    sys.stderr.write('Error:\t%s\n' % msg)
    if exit:
        sys.exit(1)

def lee_xml(archivo_passwd):
    global c_up, c_down, c_ssh, c_dns, c_http, c_https, nginx, apache, dianaea, otros_http, n_name, honeypot, ssh 
    errores = 0

    with open(archivo_passwd,'r') as hosts:
        root = ET.fromstring(hosts.read())
        for host in root.findall('host'):
            status = host.find('status').get('state')
            honeypot = ' '
            ssh = ' '
            if status == 'up':
                c_up += 1                
            if status == 'down':
                c_down += 1             
            ip = host.find('address').get('addr')
            #print (ip)
            for elem in host.iter():
                if elem.tag == "hostname":
                    hostname = elem.attrib['name']
                    n_name += 1
                else:
                    #print ('No encuentro el hostname')
                    hostname = '' #elem.tag == "hostname"
            #PUERTOS
            for port in host.iter():
                if port.tag == "port":                
                    #print port.attrib['portid']
                    n_port = port.attrib['portid']                   
                if port.tag == "state":
                    #print port.attrib['state']
                    estado_p = port.attrib['state']
                if port.tag == "service":
                    if ((n_port=='80') and (estado_p=='open')):
                        try:
                            if port.attrib['product']:
                                #print port.attrib['product']
                                http_prod = port.attrib['product']
                                if http_prod == "Apache httpd":
                                    apache += 1
                                if http_prod == "nginx":
                                    nginx += 1
                                if http_prod == "Dionaea Honeypot httpd":
                                    #honeypot = 'Si'
                                    dianaea += 1
                                #if http_prod != "Dionaea Honeypot httpd":
                                 #   honeypot = ' '
                                else:
                                    otros_http += 1
                        except:
                            errores += 1
                    #SSH
                    if ((n_port=='22') and (estado_p=='open')):
                        ssh = 'Si'
                        c_ssh += 1
                    if ((n_port=='22') and (estado_p=='close')):
                        ssh = ' '
                     #   print ('No estoy contando en SSH')
                    #DNS
                    if ((n_port=='53') and (estado_p=='open')):
                        c_dns += 1
                    #else:
                     #   print ('No estoy contando en DNS')
                    #HTTP
                    if ((n_port=='80') and (estado_p=='open')):
                        c_http += 1
                        if http_prod == "Dionaea Honeypot httpd":
                            honeypot = 'Si'
                        if http_prod != "Dionaea Honeypot httpd":
                            honeypot = ' '           
                    #else:
                     #   print ('No estoy contando en HTTP')
                    #HTTPS
                    if ((n_port=='443') and (estado_p=='open')):
                        c_https += 1
                    #else:
                     #   print ('No estoy contando en HTTPS')
            equipo = Hosts(status,ip,hostname,honeypot,ssh)
            equipos.append(equipo)                 
        print 'Equipos Encendidos: %s' %(c_up)
        print 'Equipos Apagados: %s ' % (c_down)
        print 'Equipos con puerto 22 abierto: %s' % (c_ssh)
        print 'Equipos con puerto 53 abierto: %s' % (c_dns)
        print 'Equipos con puerto 80 abierto: %s' % (c_http)
        print 'Equipos con puerto 443 abierto: %s' % (c_https)
        print 'Equipos con Nombre de dominio: %s' % (n_name)
        print 'Servidores HTTP con Apache: %s' % (apache)
        print 'Servidores HTTP con Dionaea: %s' % (dianaea)
        print 'Servidores HTTP con Nginx: %s' % (nginx)
        print 'Servidores HTTP con otros productos: %s' % (otros_http)

def reporte_csv(archivo_reporte):
    with open(archivo_reporte, 'wb') as output:
        output.write( 'Status,IP,Name_Domain,Honeypot,SSH' + '\n')
        map(lambda u: output.write(str(u)),equipos)
        
def escribe_reporte(archivo_reporte):
    sys.stdout = open(archivo_reporte, 'w')
    print (datetime.now())
    md5(sys.argv[1])
    sha1(sys.argv[1])
    print 'Equipos Encendidos: %s' %(c_up)
    print 'Equipos Apagados: %s ' % (c_down)
    print 'Equipos con puerto 22 abierto: %s' % (c_ssh)
    print 'Equipos con puerto 53 abierto: %s' % (c_dns)
    print 'Equipos con puerto 80 abierto: %s' % (c_http)
    print 'Equipos con puerto 443 abierto: %s' % (c_https)
    print 'Equipos con Nombre de dominio: %s' % (n_name)
    print 'Servidores HTTP con Apache: %s' % (apache)
    print 'Servidores HTTP con Dionaea: %s' % (dianaea)
    print 'Servidores HTTP con Nginx: %s' % (nginx)
    print 'Servidores HTTP con otros productos: %s' % (otros_http)
 
if __name__ == '__main__':
    if len(sys.argv) != 3:
        printError('Indicar archivo a leer y archivo de reporte.', True)
    print (datetime.now())
    md5(sys.argv[1])
    sha1(sys.argv[1])
    lee_xml(sys.argv[1])
    escribe_reporte(sys.argv[2])
    reporte_csv("reporte.csv")