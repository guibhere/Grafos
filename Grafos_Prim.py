# -*- coding: cp1252 -*-
import os
A = 0
B = 0
def matrix(tam):
    print "Insira a Matriz"
    M = []
    for i in range(tam):
        l = raw_input().split()
        M.append(l)
    return M

def matrix0(tam):
    M = []
    for i in range(tam):
        l = []
        for j in range(tam):
            l.append(0)
        M.append(l)
    return M

def matrix_vetor(M,tam):
    k=0
    V = []
    for i in range(tam):
        for j in range(tam):
            V.append(int(M[i][j]))        
    #print V      
    return V

def vetor_matrix(V,tam):
    M = matrix0(tam)
    k=0
    for i in range(tam):
        for j in range(tam):
            M[i][j] = int(V[k])
            k+=1
    return M

def matrix_adj(M,tam):
    abs = 0
    R = matrix0(tam)
    for i in range(tam):
        for j in range(tam):
            if(int(M[i][j])>abs):
                abs = int(M[i][j])
                
    for i in range(tam):
        for j in range(tam):
            if(int(M[i][j])<abs):
               R[i][j] = 1
               
            else:
               R[i][j] = 0 
    return R        
            
def lista_arestas(M,tam):
    
    L=[]
    A = matrix_adj(M,tam)
    #for i in range(tam):
     #   print A[i]
    aux = 0

    for i in range(tam):
        aux+=1
        for j in range(tam):
            if((j>i)and(int(A[i][j])>0)):
             R = []
             R.append(i)
             R.append(j)
             R.append(int(M[i][j]))
             L.append(R)
    L.sort(key=lambda x: x[2])

    return L

def v1v2(M,tam):
    flag=0
    for i in range(tam):
        if(flag==1):
            break
        for j in range(tam):
            if(int(M[i][j])==1):
                v1 = i
                v2 = j
                flag=1
                break
          
    return v1,v2 

def simple(M,tam):
    for i in range(tam):
        for j in range(tam):
            if(i==j):
                M[i][j] = 0
            else:
                if(int(M[i][j])>1):
                    M[i][j] = 1
                    
    return M

def desconexo(M,tam):
    soma=0
    for i in range(tam):
        for j in range(tam):
            soma+=int(M[i][j])
    if (soma==0):
        return True
    else:

        return False
    
def fusao(M,tam):
    if(tam>1):
        if(desconexo(M,tam)==True):
            #print "Desconexo (",tam," Componente(s) Conexos)"
            return tam
        M = simple(M,tam)
        v1,v2 = v1v2(M,tam)
        #print "Fusão : (V",v1+1,",V",v2+1,")"
        
        
    
        linha = []
        coluna = []
        V = matrix_vetor(M,tam)
        S = []
        for i in range(tam):
               if(i!=v2):
                coluna.append(int(M[i][v1]) + int(M[i][v2]))
               if(i!=v2):
                linha.append(int(M[v1][i]) + int(M[v2][i]))

               
                   
        #print "linha",linha
        #print "coluna",coluna
        a=b=k=0
        for i in range(tam):
            for j in range(tam):
                if(v2*tam<=k<(v2*tam)+tam)or(k==(i*tam)+v2):
                     k+=1
                else:
                     if(v1*(tam)<=k<(v1*tam)+tam):
                       # print "linha",linha[a],k
                        S.append(int(linha[a]))
                        if(i==j):
                         a+=1
                         b+=1
                        else:
                            a+=1
                     elif(k==i*tam+v1):
                         #print "coluba",coluna[b],k 
                         S.append(int(coluna[b]))
                         b+=1
                     else:
                        #print"add M",k
                        S.append(int(V[k]))
                     k+=1        
                
        #print V
        #print S
        R = vetor_matrix(S,tam-1)         
        #print 
        R= simple(R,tam-1)
        #for i in range(tam-1):
         #   print R[i]
        #print
        return fusao(R,tam-1)
        
    else:
        #print "CONEXO"
        return tam   
    
def list_adj(A,tam):
    adj = []
    for i in range(tam):
        add = []
        for j in range(tam):
            if(A[i][j]>0):
                add.append(j)
        adj.append(add)
    return adj   
    
def iscycle(R,E,tam):
    x = E[0]
    y = E[1]
    C = conj(R)
    L = []
    flag = 0
    #print "R = " ,R
    M1 = matrix_Con(R,tam)
    for i in range(len(R)):
     L.append(R[i])
    L.append(E)
    M2 = matrix_Con(L,tam)
    #print "M1"
    #for i in range(tam):
     #   print M1[i]
    #print "M2"    
    #for i in range(tam):
        #print M2[i]
 
      
    for i in range(len(C)):
        if(x==C[i])or(y==C[i]):
            flag+=1
            
    if(flag<2):
        #print "NAO Forma Ciclo : ",E
        return True
    else:
        A = fusao(M1,tam)
        B = fusao(M2,tam)
        #print "M1 : ",A," M2 : ",B
        if(A!=B):
         return True
        else:
         return False
    
        
def conj(R):
    dict = {}
    l = []
    for i in range(len(R)):
        l.append(int(R[i][0]))
        l.append(int(R[i][1]))
    for word in l:
        dict[word] = 1
    l[:] = dict.keys()    
    return l

def matrix_Con(R,tam):
    
    
    M = matrix0(tam)
    
    for i in range(len(R)):
        x = R[i][0]
        y = R[i][1]
        M[x][y] = 1
        M[y][x] = 1
        
    return M
    
def ord_arestas(l):        
    
    l.sort(key=lambda x: x[2])   
    return l

def caminho(M,tam):
    c =0
    L = lista_arestas(M,tam)
    #print "L :",L
    C = []
    C.append(0)
    R = []
    
    for c in range(len(L)):
        P = []
        for i in range(len(C)):     
            for j in range(len(L)):
                if(C[i] ==L[j][0])or(C[i]==L[j][1]):
                    P.append(L[j])
        P = ord_arestas(P)
        #print "P :",P
            
        for i in range(len(P)):
            if(iscycle(R,P[i],tam)):
            #print "add",L[i]
             R.append(P[i])
             C = conj(R)
             
             #print "Conjunto :",C
             break
        if(c==tam-1):
            break
                              
                                 
                                 
                                 
    return R    
    
     


def main():
    
    t = int(raw_input("Tamanho da Matriz : "))
    print "OBS: Em caso de não existir caminho entre 2 vertices inserir um valor de custo mais alto que o resto ,que seja igual pra todos os caminhos não existentes"
    print
    M = matrix(t)
    print
 
    R = caminho(M,t)
    print "Arestas Da Arvore SPANNING"
    for i in range(len(R)):
     print "A",i+1,"(","Vertice ",R[i][0]," , Vertice ",R[i][1]," , Custo ",R[i][2],")"
    print 
    soma =0
    for i in range(len(R)):
        soma += R[i][2]
    print "Peso Total da Arvore SPANNING :",soma
    print

    G = matrix0(t)
    c = 0
    for i in range(len(R)):
        x = R[i][0]
        y = R[i][1] 
        G[x][y] = 1
        G[y][x] = 1
    print "Matriz ADJ da Arvore SPANNING :"    
    for i in range(t):
       print G[i]
    os.system("pause")   
            
                
        
    


if __name__ == "__main__":
    main()
