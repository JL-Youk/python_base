import hashlib, os, random, struct, base64, urllib, sys, glob, os.path, chunky
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
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

cipher = AESCipher(key='issou')
adresse= "C:\Users\jeanl\Documents\GitHub\python_base\crypto\ctest"

def gocrypt(imp):
    print imp
    mon_fichier = open(imp, "r")
    contenu = mon_fichier.read()
    encrypted = cipher.encrypt(contenu)
    mon_fichier = open(imp, "w")
    mon_fichier.write(encrypted)
    mon_fichier.close()

def godecryp(imp):
    print imp
    mon_fichier = open(imp, "r")
    contenu = mon_fichier.read()
    deencrypted = cipher.decrypt(contenu)
    mon_fichier = open(imp, "w")
    mon_fichier.write(deencrypted)
    mon_fichier.close()


def test2(source, destination):
    print "yo"

def cryptdocument():
    for element in os.listdir(adresse):
        if element.endswith('.html'):
            complet = adresse + element
            gocrypt(complet)

def decryptdocument():
    for element in os.listdir(adresse):
        if element.endswith('.html'):
            complet = adresse + element
            godecryp(complet)

def test():
    for element in os.listdir(adresse):
        if element.endswith('.txt'):
            source = adresse + element
            destination = adresse + 'out.txt'
            test2(source,destination)

def magique():
    NUM_OF_LINES=9999999
    filename = 'C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\1.txt'
    with open(filename) as fin:
        fout = open("C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\output0.txt","wb")
        for i,line in enumerate(fin):
            print "original" + line
            line = cipher.encrypt(line)
            print "crypte" + line
            print ""
            print ""
            fout.write(line+ "\r\n")
            if (i+1)%NUM_OF_LINES == 0:
                fout.close()
                fout = open("C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\output%d.txt"%(i/NUM_OF_LINES+1),"wb")
        fout.close()

def magiquedecrypte():
    NUM_OF_LINES=9999999
    filename = 'C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\output0.txt'
    with open(filename) as fin:
        fout = open("C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\outputNEW0.txt","wb")
        for i,line in enumerate(fin):
            print line
            line = cipher.decrypt(line)
            print line
            fout.write(line+ "\r\n")
            if (i+1)%NUM_OF_LINES == 0:
                fout.close()
                fout = open("C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\outputNEW%d.txt"%(i/NUM_OF_LINES+1),"wb")
        fout.close()


print "1 pour crypter"
print "2 pour decrypter"
print "3 pour test"
print "4 pour magique"
print "5 pour magique decrypt"
n1 = input()
if n1 == 1:
    cryptdocument()

elif n1 == 2:
    decryptdocument()

elif n1 == 3:
    test()

elif n1 == 4:
    magique()

elif n1 == 5:
    magiquedecrypte()
