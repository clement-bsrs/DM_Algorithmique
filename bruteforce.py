solution = []

def tous_differents(sol):
    for i in range(len(sol)):
        for j in range(len(sol)):
            if(sol[i] == sol[j]):
                return False
            
def calcul(sol):
    if ( (sol[0]*1000 + sol[1]*100 +sol[2]*10 + sol[3]) 
       + (sol[5]*1000 + sol[6]*100 + sol[7]*10 + sol[8])
       == (sol[10]*10000 + sol[11]*1000 + sol[12]*100 + sol[13]*10 + sol[14])
       ):
        return True

def affiche(tab):
    for i in range(0, len(tab)):
        print(tab[i])
    
    
def brutality():
    
    #! coca + cola = pepsi
    #?caractère unique : c o a l p e s i
    compteur = 0
    for c in range(10):
        for o in range(10):
            if(o!=c):
                for a in range(10):
                    if(a!=c and a!=o):
                        for l in range(10):
                            if(l!=c and l!=o and l!=a):
                                for p in range(10):
                                    if(p!=c and p!=o and p!=a and p!=l):
                                        for e in range(10):
                                            if(e!=c and e!=o and e!=a and e!=l and e!=p):
                                                for s in range(10):
                                                    if(s!=c and s!=o and s!=a and s!=l and s!=p and s!=e):
                                                        for i in range(10):
                                                            if(i!=c and i!=o and i!=a and i!=l and i!=p and i!=e and i!=s):
                                                            
                                                                #print(c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i)
                                                                if calcul([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i]):
                                                                    solution.append([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i])
                                                                    compteur=compteur + 1
    
    print("nombre de solution = ", compteur)

def exec_brutality():
    brutality()
    affiche(solution)

exec_brutality()