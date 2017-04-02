import hashlib, os, random, struct, base64, urllib, sys, glob, os.path, chunky, webbrowser, getpass
# from ggplot import aes

global key
global adresse
global ext

key  = 'risitas'
adresse = "C:\\Users\\"+getpass.getuser()+"\\Desktop\\test\\1.txt"
ext = [
    '.txt', '.pdf', '.png'
]

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    filename, file_extension = os.path.splitext(in_filename)
    if file_extension in ext:
        if not out_filename:
            out_filename = in_filename + '.crypt'
        iv = os.urandom(16)
        # encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)
        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    # outfile.write(encryptor.encrypt(chunk))
                    outfile.write(chunk)
        outfile.close()
        infile.close()
        try:
            os.remove(in_filename)
            os.rename(out_filename, in_filename)
        except WindowsError:
            print "WinError"

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    filename, file_extension = os.path.splitext(in_filename)
    if file_extension in ext:
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0]
        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            # decryptor = AES.new(key, AES.MODE_CBC, iv)
            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    # outfile.write(decryptor.decrypt(chunk))
                    outfile.write(chunk)
                outfile.truncate(origsize)
        outfile.close()
        infile.close()
        try:
            os.remove(in_filename)
            os.rename(out_filename, in_filename)
        except WindowsError:
            print "WinError"


def cryptdocument():
    encrypt_file(key, adresse)
    print "Encrypting " + adresse

def decryptdocument():
    decrypt_file(key, adresse)
    print "Decrypting " + adresse

def magique():
    NUM_OF_LINES=9999999
    filename = 'C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\1.txt'
    with open(filename) as fin:
        fout = open("C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\output0.txt","wb")
        for i,line in enumerate(fin):
            print line
            fout.write(line)
            if (i+1)%NUM_OF_LINES == 0:
                fout.close()
                fout = open("C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\output%d.txt"%(i/NUM_OF_LINES+1),"wb")
        fout.close()

def magiquedecrypte():
    NUM_OF_LINES=99999999
    filename = 'C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\output0.txt'
    with open(filename) as fin:
        fout = open("C:\\Users\\jlf\\Documents\\GitHub\\python_base\\crypto\\ctest\\outputNEW0.txt","wb")
        for i,line in enumerate(fin):
            print line
            fout.write(line)
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
