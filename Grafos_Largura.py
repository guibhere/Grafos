# -*- coding: cp1252 -*-
import os
def matrix(tam):
    print "Insira a Matriz de adjacencia"
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

def lista_arestas(tam):
    L = []
    for i in range(tam):
        a,b = raw_input().split()
        l = [a,b]
        L.append(l)
        l = [b,a]
        L.append(l)
    return L

def list_adj2(A,tam):
    Adj = []
    for i in range(tam):
      l = []
      for j in range(len(A)):
         if (i==int(A[j][0])):
             l.append(int(A[j][1]))
             #print A[j][0]
      Adj.append(l)

   # for i in range(len(Adj)):
         #print "V",i," : ",Adj[i]
    return Adj 
    
def list_adj(M,tam):
    adj = []
    for i in range(tam):
        add = []
        for j in range(tam):
            
            if(int(M[i][j])>0):
                add.append(j)
                #print j
        adj.append(add)
    return adj   
def isall(l):
    flag = 0
    for i in range(len(l)):
        if(l[i]==-1):
            flag = 1
            break
    #print l    
    if (flag==1):
        return False
    else:
        return True
def isend(L,c):
    flag = 0
    for i in range(len(L)):
        if(L[i]==c):
            return False
    return True    
        
def busca_largura(Ladj,tam,p,d):
    label = []
    for i in range(tam):
        label.append(-1)
    label[p] = int(0)
    c = 0
    while(isall(label)==False):
        for i in range(tam):
            if(label[i]==c):
                va = i
                
                adj = Ladj[va]
                #print va," :",adj
                for j in range(len(adj)):
                    v = adj[j]
                    if(label[v] ==-1):
                        label[adj[j]] = c+1
                       # print adj[j],label[adj[j]]
        c+=1
        if(isend(label,c)):
         break
    return label    

def backtracking(L,Ladj,p,d):
    c = L[int(d)]
    va = int(d)
    caminho = []
    caminho.append(va)
    #print c

    while(c>=0):
        adj = sorted(Ladj[va])
        
        for i in range(len(adj)):
            v = adj[i]
            if(L[v]==(c-1)):
                va = adj[i]
                #print va
                caminho.append(va)
                break
        c-=1
    showmetheway = []   
    for i in range(len(caminho)):
        vc = caminho.pop()
        
        vc = chr(vc+65)
            
        showmetheway.append(vc)
    return showmetheway            
        
def num_caminhos(L,Ladj,p,d):
    u = []
    c = L[int(d)]
    va = int(d)
    for i in range(len(L)):
      if(i==int(d)):
          u.append(1)
      else:
          u.append(0)
    while(c>=0):
        #print "iteração",c
        for i in range(len(L)):
            if(L[i]==c-1):
                v = i
                adj = Ladj[v]
                soma = 0
                #
                for j in range(len(adj)):
                  vv = adj[j]
                  #print chr(v+65),"adj",chr(vv+65)
                  if(L[vv]>L[v]):
                      soma = soma + u[vv]
                      #print u[vv]
                u[v] = soma

        c-=1
    return u   
    



def main():
    op = int(raw_input("Deseja Inserir por matriz de adjacencia ou arestas?(1-matriz/2-arestas) : "))
    if(op==1):
        t = int(raw_input("Insira o numero de vertices : "))
        M = matrix(t)
        LA = list_adj(M,t)
    elif(op==2):
         t = int(raw_input("Insira o numero de vertices : "))
         ta = int(raw_input("Insira o numero de Arestas : "))
         print "Insira as arestas : "
         La = lista_arestas(ta)
         LA =  list_adj2(La,t)
        

        

    print 
    p,d=(raw_input("Insira a partida e o destino : ").split())
    L = busca_largura(LA,t,int(p),int(d))
    cont = 0
    for i in range(len(L)):
        if(L[i]==-1):
        
               print "Vertice : ",chr(cont+65),"(Impossivel Chegar)"
               cont+=1
        else:       
     
            
             print "Vertice : ",chr(cont+65),"(",L[i],")"
             cont+=1
    if(L[int(d)]==-1):
       print "Não é possivel chegar ao destino"
    else:  
        print "Comprimento mais curto :",L[int(d)]
        caminho =  backtracking(L,LA,p,d)
        print "Caminho Possivel : ",caminho
        u = num_caminhos(L,LA,p,d)
        print "Numero de caminhos mais curtos :",u[int(p)]
        print u 
    os.system("pause")
       
        
    





if __name__ == "__main__":
    main()
        
