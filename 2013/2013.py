from pickle import dump , load

def f(x):
    return x*x
    
def saisir():
    eps = float(input("eps = "))
    while eps <0.001 or eps >0.1:
        eps = float(input("eps = "))
    return eps



def remplire(txt ,eps):
    F = open(txt,"wb")
    e = {}
    N = 1
    e["n"] = N
    e["trap"] = trap(N)
    e["rect"] = rect(N)
    dump(e,F)
    while (abs(trap(N) - 9) > eps) and (abs(rect(N) - 9) > eps):
        N += 1
        e["n"] = N
        e["trap"] = trap(N)
        e["rect"] = rect(N)
        dump(e,F)
    F.close()

def rect(N):
    h = 3/N
    s = 0
    x = 0
    for i in range(N):
        s+= f(x)
        x+=h
    return s*h

def trap(N):
    h = 3/N
    s = 0
    x = 0
    for i in range(N):
        s+= (f(x)+f(x+h) )/2
        x+=h
    return s*h
def afficher(txt,eps):
    F = open(txt,"rb")
    eof = False
    while eof == False:
        try:
            line = load(F)
            print("nb sub divisions = ",line["n"],"methode trapeze = ",line["trap"],"methode rectangle = ",line["rect"])
        except:
            eof = True
    if(abs(line["trap"] - 9) < abs(line["rect"] - 9)):
        print("la methode de trapeze est plus precive avec ",line["n"] ,"subdivion et un resutat de ",line["trap"])
    else:
        print("la methode de rectangle est plus precive avec ",line["n"] ,"subdivion et un resutat de ",line["rect"])
#pp
eps = saisir()
remplire("Calcul.dat",eps)
afficher("Calcul.dat",eps)