# -*- coding: cp1252 -*-
import os
def matrix(tam):
    print "Insira a Matriz de adjacencia"
    M = []
    for i in range(tam):
        l = raw_input().split()
        M.append(l)
    return M

def list_arestas(M):
    A = []
    for i in range(len(M)):
       
        for j in range(len(M)):
            l = []
            
            if(int(M[i][j])<99):
                l.append(i)
                l.append(j)
                A.append(l)
    #for i in range(len(A)):
    #    print A[i]
    return A

def matrixc(A,tam):
    M = []
    for i in range(tam):
        l = []
        for j in range(tam):
            if(int(A[i][j])<99):
             l.append(i)
            else:
             l.append(-1)
        #print l     
        M.append(l)
    return M    
                
    
def Caminho(A,M,tam):

    for k in range(tam):
        for i in range(tam):
            for j in range(tam):
                if(i!=j):
                    
                    if (int(A[i][k]) + int(A[k][j]) < int(A[i][j])):
                        A[i][j] = int(A[i][k]) + int(A[k][j])
                        M[i][j] = M[k][j]
    return A,M

def main():
     t = int(raw_input("Insira o numero de vertices : "))
     print("Utilizar 99 para caminhos infinitos")
     A = matrix(t)
     M = matrixc(A,t)
     A,M = Caminho(A,M,t)
##     print "Matriz CUSTO:"
##     for i in range(t):
##         print A[i]
##     print "Matriz CAMINHOS:"    
##     for i in range(t):
##         print M[i]
     (p),(d) =  (raw_input("Insira a partida e o destino : ").split())
     va = int(d)        
     L = M[int(p)]
     C = []
     C.append(int(d))
     while(va!=int(p)):
         va  = L[va]
         C.append(va)

         
     print "Distancia Caminho (",p,"->",d,")",":",A[int(p)][int(d)]    
     for i in range(len(C)-1,-1,-1):
         if(i>0):
             print C[i],"->",
         else:
             print C[i],"!"
     os.system("pause")        





if __name__ == "__main__":
    main()
