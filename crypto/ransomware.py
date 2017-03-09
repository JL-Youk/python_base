from Crypto.Hash import SHA256
import urllib, os, sys
# ouvre une image trouver sur internet
urllib.urlretrieve("http://image.noelshack.com/fichiers/2017/07/1487081804-risitas-1er-script.png", "a.png")
os.startfile("a.png")


hash = SHA256.new()
hash.update('aa')
print hash.digest()
