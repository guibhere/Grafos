# -*- coding: cp1252 -*-
import os

global inf
inf = 99
def matrix(tam):
    print "Insira a Matriz de adjacencia"
    print
    M = []
    for i in range(tam):
        l = raw_input().split()
        M.append(l)
    return M

def lista_profundidade(tv):
    L = []
    for i in range(tv):
        l = []
        l.append(0)
        l.append(0)
        L.append(l)
    return L
def visitados(LP,adj):
    nv = []
    for i in range(len(adj)):
        va = adj[i]
        if(LP[va][0]==0):
            nv.append(va)
    nv = sorted(nv)        
    return nv[0]        

def isfim(LP,va,adj):
    flag = 0
    for i in range(len(adj)):
        v = adj[i]
        if(LP[v][0]!=0):
            flag +=1
    if(flag==len(adj)):
        return True
    else:
        return False

def busca_profundidade(A,tam):
    LAdj = lista_adj(A,tam)
    LP = lista_profundidade(tam)
    va = 0
    c = 0
    Pilha = []

    while(c<tam*2):
    
        
        
        if(LP[va][0]==0):
            c+=1
            Pilha.append(va)
            LP[va][0]=c
            #print va ," visitado t=",c
            
        adj = LAdj[va]
        
        if(len(adj)==0):

            c+=1
            Pilha.pop()
            LP[va][1]= c
            #print va," finalizado t=",c
            #print "len",len(Pilha)
            if(len(Pilha)>0):

                va = Pilha.pop()
                Pilha.append(va)
            else:
               
                for i in range(len(LP)):
                    if(LP[i][0]==0):
                        va = i
                        break
            
            
        else:
            if(isfim(LP,va,adj)):  
              c+=1
              Pilha.pop() 
              LP[va][1]= c
              #print va," finalizado t=",c
              if(len(Pilha)>0):
                  va = Pilha.pop()
                  Pilha.append(va)
              else:
               
                for i in range(len(LP)):
                    if(LP[i][0]==0):
                        va = i
                        break    
            else:
              va = visitados(LP,adj)
        
    return Ord_Top(LP)

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
    
def GAO(M,Adj,A,p,K):
    D = []
    Pai = []

    for i in range(len(Adj)):
        Pai.append(-1)
        if(i==int(p)):
            D.append(0)
        else:
            D.append(inf)
    

    for i in range(len(K)):
        v = K.pop()
        v1 = v[0]
        adj = Adj[v1]
        for j in range(len(adj)):
            v2 = adj[j]
            d = int(M[v1][v2])
            Pai,D = RELAX(v1,v2,d,Pai,D)
    return Pai,D

def lista_adj(A,tv):
    Adj = []
    for i in range(tv):
      l = []
      for j in range(len(A)):
         if (i==int(A[j][0])):
             l.append(int(A[j][1]))
             #print A[j][0]
      Adj.append(l)

   # for i in range(len(Adj)):
         #print "V",i," : ",Adj[i]
    return Adj  
           
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
    
def Ord_Top(LP):
    Ord = []
    for i in range(len(LP)):
       
        vis = LP[i][0]
        fin = LP[i][1]
        ver = i
        l = [ver,vis,fin]
        Ord.append(l)
    Ord.sort(key=lambda x: x[2])
    #print "Ordem Topologica : ",Ord
    return Ord
        
def main():
     t = int(raw_input("Insira o numero de vertices : "))
     print
     M = matrix(t)
     p,d = (raw_input("Insira a partida e o destino : ").split())
     print
     Adj,A= list_adj(M)
     K = busca_profundidade(A,t)
     Pai,D = GAO(M,Adj,A,p,K)
     print "Distancias : ",D
     print "Pais : ",Pai
     C = []
     C = Caminho(D,Pai,p,d,C)
     print "Caminho (",p,"->",d,") : ","Distancia = ",D[int(d)]
     for i in range(len(C)-1,-1,-1):
         if(i>0):
          print C[i],"->",
         else:
             print C[i],"!"
     os.system("pause")
     
if __name__ == "__main__":
    main()
