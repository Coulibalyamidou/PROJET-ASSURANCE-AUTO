from math import*
print("equation de premier degré dans R")
a=float(input("entrer a="))
b=float(input("entrer b="))
if a==0:
    print("ERREUR! LE REEL DOIT ETRE DIFFERENT DE ZERO")
elif b==0:
    print(a,"x","+",(b),"=",0,"a pour solution x=",0)
else:
    x=-b/a
    print("L'équation est:",a,"*","x","+",(b),"=" ,0)
    print("La solution de l'équation est x =",round(x,2))
