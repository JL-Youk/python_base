import socket
hote = "10.94.73.114"
port = 15555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nom = raw_input("c'est quoi ton nom?\n")
socket.connect((hote, port))
# print "Connection on {}".format(port)
while True:
    rep = raw_input()
    reponces = nom + ' : ' + rep
    socket.send(reponces)

#
# print "Close"
# socket.close()
