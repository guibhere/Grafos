# -*- coding: cp1252 -*-
import os
def lista_arestas(tam):
    L = []
    print 
    print "Insira as Aresta : (v1 v2)"
    print 
    for i in range(tam):
        l = raw_input().split()
        L.append(l)
    return L

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
        
    return LP


        

        
def main():
    tv = int(raw_input("Numero de Vertices : "))
    print 
    ta = int(raw_input("Numero de Arestas : "))
    A = lista_arestas(ta)
   
    P = busca_profundidade(A,tv)
    for i in range(len(P)):
               print "Vertice : ",chr(i+65),"(",P[i][0],"/",P[i][1],")"
    os.system("pause")

if __name__ == "__main__":
    main()
