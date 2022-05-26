from numpy import zeros

def remplire(M,txt):
    F = open(txt,"r")
    i = 0
    line = F.readline()
    while line != "":
        for j in  range(10):
            M[i,j] = line[:line.find(" ")]
            line = line[line.find(" ")+1 :]
        i+=1
        line = F.readline()
    F.close()
    return i

def Trie (d, f ,M):
    T=[0 for x in range(f)]
    for i in range(10):
        for k in range(f):
            T[k] = int(M[k,i])
        Tri_Rapide (d,f,T)
        for k in range(f):
            M[k,i] = int(T[k])

def Tri_Rapide (d, f ,T):
    if(f>d):
        m = (d+f) // 2
        T[m] , T[d] = T[d] , T[m]
        p = d
        for i in range(d+1,f):
            if T[i] < T[d]:
                p += 1
                x =  T[i]
                T[i]=T[p]
                T[p]=x
        T[p] , T[d] =T[d] , T[p]
        Tri_Rapide(d, p-1, T)
        Tri_Rapide(p+1, f, T)

def remplireF(M,i,txt):
    F = open(txt,"w")
    for x in range(i):
        msg = ""
        for j in range(10):
            msg+= str(int(M[x,j]))+" "
        F.write(msg+"\n")

def afficher(txt):
    F = open(txt,"r")
    line = F.readline()
    print(line)
    while line != "":
        line = F.readline()
        print(line[:-1])
    F.close()

#PP

M = zeros((20,10))
i = remplire(M,"Source.txt")
Trie(0,i,M)
remplireF(M,i,"Resultat.txt")
afficher("Resultat.txt")