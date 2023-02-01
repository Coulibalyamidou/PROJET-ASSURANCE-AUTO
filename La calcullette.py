def add(x,y):
    return (x+y)
def soust(x,y):
    return (x-y)
def mult(x,y):
    return (x*y)
def div(x,y):
    return(x/y)
print("1:addition,2:multiplication,3:soustraction,4:division")

#
x=float(input("donner x="))
y=float(input("donner y="))
op=int(input("entrer l'operateur à effectuer "))
if op==1:
    print(x,"+",y,"=",add(x,y))
elif op==2:
    print(x,"*",y,"=",mult(x,y))
elif op==3:
    print(x,"-",y,"=",soust(x,y))
elif op==4:
    if y==0:
        print("impossible y doit être différent de zéro")
    else:
        print(x,"/",y,"=",div(x,y))
else:
    print("operateur inconnu")
