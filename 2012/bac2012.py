import numpy as np
from pickle import load , dump

def saisirN():
    N = int(input("N = "))
    while N < 2 or N >100:
        N = int(input("N = "))
    return N

def saisirP():
    P = int(input("P = "))
    while P < 2 or P > 6:
        P = int(input("P = "))
    return P

def remplireF(N,P,txt):
    F = open(txt,"wb")
    for i in range(N):
        nb = int(input("number = "))
        while not( len( str(nb) ) == P ):
            nb = int(input("number = "))
        dump(nb,F)
    F.close()

def prime_factors(n):
    nb = n
    i = 2
    factors = ""
    count = 0
    while  (nb != 1):
        if(nb%i == 0):
            nb = nb/i
            count += 1
        else:
            if(count != 0): 
                factors += str(count)+str(i)
            count = 0
            i += 1
    factors += str(count)+str(i)
    return factors

def remplireF2(N,txt,txt2):
    F = open(txt,"rb")
    eof = False
    T = np.zeros(N)
    j=0
    while eof == False:
        try:
            T[j] = load(F)
            j += 1
        except:
            eof = True
    F.close()
    F = open(txt2,"w")
    for i in range (N):
        F.write(str(prime_factors( int(T[i]) ))+"\n")
    F.close()
    
def afficher(N,txt):
    F = open(txt,"r")
    line = F.readline()
    while not( line == "" ):
        print(line)
        line = F.readline()
    F.close()

#pp

N = saisirN()
P = saisirP()
remplireF(N,P,"Nombres.dat") 
remplireF2(N,"Nombres.dat","Facteurs.txt")
afficher(N,"Facteurs.txt")