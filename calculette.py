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
print calcule(n1, typecalcule, n2)
# .-------------------.
# |                   |
# |                   |
# |  P A R E N T A L  |
# |                   |
# |  A D V I S O R Y  |
# |                   |
# |                   |
# | explicit  content |
# |                   |
# `-------------------'
