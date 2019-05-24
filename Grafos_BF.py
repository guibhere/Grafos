# -*- coding: cp1252 -*-
import os
global inf
inf = 99
def matrix(tam):
    print "Insira a Matriz de adjacencia"
    print "OBS : Utilizar 99 para caminhos inexistentes"
    print
    M = []
    for i in range(tam):
        l = raw_input().split()
        M.append(l)
    return M


def list_adj(M):
    Adj = []
    A = []
    

    
    for i in range(len(M)):
        Adj.append([])
        for j in range(len(M)):
            l = []
            l.append(i)
            l.append(j)
            l.append(int(M[i][j]))
            if(int(M[i][j])<99):
                Adj[i].append(int(j))
                A.append(l)
    return Adj,A

def RELAX(v1,v2,d,Pai,D):
    if(D[v2]>D[v1] + d):
        D[v2] = D[v1] + d
        Pai[v2] = v1
    return Pai,D
    
def B_F(M,Adj,A,p):
    D = []
    Pai = []

    for i in range(len(Adj)):
        Pai.append(-1)
        if(i==int(p)):
            D.append(0)
        else:
            D.append(inf)
    

    for i in range(len(M)):
        for j in range(len(A)):
            v1 = A[j][0]
            v2 = A[j][1]
            d = A[j][2]
            Pai,D = RELAX(v1,v2,d,Pai,D)
    for i in range(len(Adj)):
       v1 = A[i][0]
       v2 = A[i][1]
       d = A[i][2]
       if(D[v2]>D[v1]+d):
         print "Possui Ciclo Negativo"
         return D,Pai
    print "Não Possui Ciclo Negativo"
    return D,Pai
   
def Caminho(D,P,p,d,C):
    if(int(p)==int(d)):
        C.append(p)
        return C
    elif(P[int(d)]==-1):
        print "Não ha caminho"
        return
    else:
        C.append(d)
        return Caminho(D,P,p,P[int(d)],C)

def main():
     t = int(raw_input("Insira o numero de vertices : "))
     print
     M = matrix(t)
     p,d = (raw_input("Insira a partida e o destino : ").split())
     print
     Adj,A= list_adj(M)
     D,P = B_F(M,Adj,A,p)
     print "Distancias : ",D
     print "Pais : ",P
     C = []
     C = Caminho(D,P,p,d,C)
     print "Caminho (",p,"->",d,") : ","Distancia = ",D[int(d)]
     for i in range(len(C)-1,-1,-1):
         if(i>0):
          print C[i],"->",
         else:
             print C[i],"!"
     os.system("pause")
if __name__ == "__main__":
    main()
