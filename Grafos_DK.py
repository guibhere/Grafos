# -*- coding: cp1252 -*-
import os

def matrix(tam):
    print "Insira a Matriz de adjacencia"
    print
    M = []
    for i in range(tam):
        l = raw_input().split()
        M.append(l)
    return M


def list_adj(A,tam):
    B = []
    ADJ = []
    maxx =99
    for i in range(tam):
     for j in range(tam):
          if(j<i):
              j=i
          if(int(A[i][j])<maxx):
              B.append([i,j,A[i][j]])
        
    for i in range(tam):
        v = []
        ADJ.append(v)
    for i in range(len(B)):
        v1 = int(B[i][0])
        v2 = int(B[i][1])
        ADJ[v1].append(v2)
        ADJ[v2].append(v1)

        
         
    return ADJ,A
def is_in(v,C):
    for i in range(len(C)):
        if(v==int(C[i])):
           # print v,"esta em C"
            return True
    return False    

def get_va(Rot,C):
    lmin=[]
    
    for i in range(len(Rot)):
        if(is_in(i,C)==True):
          lmin.append([Rot[i],i])
    minn = min(lmin)
    return minn[1]
    

    
def DK(M,Adj,C,Rot,tam,Way):
    if not C:
        return Rot,Way


    va= get_va(Rot,C)
    C.remove(va)
    adj = Adj[va]
    #print "Va : ",va
    for i in range(len(adj)):
        v = adj[i]
        if(Rot[v]> Rot[va] + int(M[va][v])):
           l = [va,v]
           Way.append(l)
           #print va,"alterou",v,"de",Rot[v],"para",Rot[va] + int(M[va][v])
           Rot[v] = Rot[va] + int(M[va][v])
           

   # print Rot
    #print Way

    return DK(M,Adj,C,Rot,tam,Way)
    



    
def main():
     t = int(raw_input("Insira o numero de vertices : "))
     print
     M = matrix(t)
     p,d = (raw_input("Insira a partida e o destino : ").split())
     print
     Adj,A = list_adj(M,t)
     C = []
     Rot = []
     for i in range(t):
         C.append(i)
         Rot.append(99)
     Rot[int(p)] = 0
     
         
     Way = []
     
     Rot,Way = DK(M,Adj,C,Rot,t,Way)
     print "Rotulos : ",Rot
     #print "Caminho : ",Way
     va = int(d)
     Caminho = []
     Caminho.append(va)
     while(int(va)!=int(p)):
         for i in range(len(Way)-1,-1,-1):
             if(va==int(Way[i][1])):
                 va = Way[i][0]
                 Caminho.append(va)
                 break
     print "Caminho ","de",p,"para",d,"(distancia:",Rot[int(d)],")"
     for i in range(len(Caminho)-1,-1,-1):
      if(i!=0):   
       print(Caminho[i]),'->',
      else:
          print(Caminho[i]),"!"
     os.system("pause")   









if __name__ == "__main__":
    main()
