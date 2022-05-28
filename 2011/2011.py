

def saisirA():
    A = int(input("A= "))
    while A<=2 or A>=50000:
        A = int(input("A= "))
    return A
def saisirB(A):
    B = int(input("B= "))
    while B<=2 or B>=50000 or B<A:
        B = int(input("B= "))
    return B

def remplire(A,B,txt):
    F = open(txt,"w")
    for i in range(A,B+1):
        j = 3
        while j<i:
            if(premier(j)):
                if ( puiss(2,j) -1) == i:
                    F.write(str(i) +" = 2**"+str(j)+" -1 \n")
            j+=1
    F.close()

def puiss(a,b):
    t=1
    for i in range(b):
        t = t*a
    return t

def premier(nb):
    p = True
    i = 2
    while i < nb and p == True:
        if nb%i == 0:
            p = False
        i += 1
    return p

def afficher(txt):
    F = open(txt,"r")
    line = F.readline()
    i=0
    while line != "":
        print(line)
        line = F.readline()
        i+=1
    if(i== 0):
        print("il n'y a aucun nombre de mersenne")
#pp

A = saisirA()
B = saisirB(A)
remplire(A,B,"mersenne.txt")
afficher("mersenne.txt")
