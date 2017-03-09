from Tkinter import *
root = Tk()
f1 = Frame(root, bd=1, relief='solid')
Label(f1, text='je suis dans F1').grid(row=0, column=0)
Label(f1, text='moi aussi dans F1').grid(row=0, column=1)

f1.grid(row=0, column=0)
Label(root, text='je suis dans root').grid(row=1, column=0)
Label(root, text='moi aussi dans root').grid(row=2, column=0)
root.mainloop()
print "bienvenue dans la super mega calculette en python";
print "pour une addition tapper : 1";
print "pour une soustraction tapper : 2";
print "pour une multiplication tapper : 3";
print "pour une division tapper : 4";
typecalcule = input()
def calcule(n1, typecalcule, n2):
    if typecalcule == 1:
        return (n1 + n2);
    elif typecalcule == 2:
        return (n1 - n2)
    elif typecalcule == 3:
        return (n1 * n2)
    elif typecalcule == 4:
        return (n1 / n2)
print "premier nombre ?";
n1 = input()
print "second nombre ?";
n2 = input()
print "Le resultat est :"
