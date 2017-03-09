import hashlib, os, random, struct, base64, urllib, sys
from Crypto import Random
from Crypto.Cipher import AES

def issou():
    urllib.urlretrieve("https://frompixel.com/issou/IssouNightclubCut.mp3 ", "IssouNightclubCut.mp3 ")
    os.startfile("IssouNightclubCut.mp3 ")
    urllib.urlretrieve("http://image.noelshack.com/fichiers/2017/07/1487081804-risitas-1er-script.png", "a.png")
    os.startfile("a.png")

class AESCipher(object):
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(AESCipher.str_to_bytes(key)).digest()

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AESCipher.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        raw = self._pad(AESCipher.str_to_bytes(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw)

    def decrypt(self, enc):
        enc = enc
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))


cipher = AESCipher(key='mykey')
def gocrypt():
    mon_fichier = open("ctest/1.txt", "r")
    contenu = mon_fichier.read()
    encrypted = cipher.encrypt(contenu)
    print (contenu)
    mon_fichier = open("ctest/1.txt", "w")
    mon_fichier.write(encrypted)
    print (encrypted)
    mon_fichier.close()

def godecryp():
    mon_fichier = open("ctest/1.txt", "r")
    contenu = mon_fichier.read()
    deencrypted = cipher.decrypt(contenu)
    print (contenu)
    mon_fichier = open("ctest/1.txt", "w")
    mon_fichier.write(deencrypted)
    print (deencrypted)
    mon_fichier.close()

print "1 pour crypter"
print "2 pour decrypter"
n1 = input()

if n1 == 1:
    # issou()
    gocrypt()

elif n1 == 2:
    godecryp()
