import numpy as np

#modules

def saisir():
    ch = input("donner mot clé = ")
    while ch.upper() != ch or len(ch) <3 or len(ch) >10 or ch.find("W") != -1 or verif(ch) == False:
        ch = input("donner mot clé = ")
    return ch
def verif(ch):
    c= True
    i=0
    while i < len(ch) -1:
        if ch[i+1:].find(ch[i]) != -1:
            c =False
        i+=1
    return c
def remplire(mc,M):
    stop = len(mc)
    c = 0
    order = 65
    i = 0
    for i in range(5):
        j = 0
        while j<5:
            if c < (stop):
                M[i][j] = mc[c]
                c+=1
                j+= 1
            else:
                if (exisit(chr(order),mc) == False and chr(order) != "W"):
                    M[i][j] = chr(order)
                    order += 1
                    j+= 1
                else:
                    order += 1
def exisit(ch,mc) :
    found = False
    for i in range (len(mc)):
        if ch == mc[i]:
            found = True
    return found

def saisirmsg():
    ch = input("msg = ")
    while len(ch) == 0:
        ch = input("msg = ")
    return ch

def crypter(M,ch,txt):
    mcry =""
    for i in range(len(ch)):
        if ch[i] == " ":
            mcry += " "
        elif(ch[i] == "W"):
            mcry += pos("V",M)
        else:
            mcry += pos(ch[i],M)
    F = open(txt,"w")
    F.write(mcry)
def pos(ch,M):
    found = False
    i=0
    while i<5 and found == False:
        j = 0
        while j<5 and found == False:
            if(M[i][j] == ch):
                found = True
            else:
                j+=1
            
        i+=1
    t = str(i)+str(j)
    return t
    
#PP

mc = saisir() # saisir mot clé
M = [[str() for i in range(5)] for i in range(5)] # creation matrice
remplire(mc,M) # remplisage de la matrice
ch = saisirmsg() # saisir la phrase a crypter
crypter(M,ch,"Mess_crypte.txt") # crypter la phrase

