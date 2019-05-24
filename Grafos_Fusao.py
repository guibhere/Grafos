import os
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
def v1_v2(M,tam):
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
            
def fusao(M,tam):
    if(tam>1):
        if(desconexo(M,tam)==True):
            print "Grafo DESCONEXO : (",tam,"Componetes Conexos)"
            return M
        M = simple(M,tam)
        v1,v2 = v1_v2(M,tam)
        
        print "FUSAO : (V",v1+1,",V",v2+1,")" 
        
        
        
    
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
        print 
        R= simple(R,tam-1)
        for i in range(tam-1):
            print R[i]
        print
        fusao(R,tam-1)
        
    else:
        print "Grafo CONEXO"
        return M,tam
    
def main():
    t = int(raw_input("Tamanho da Matriz : "))
    
    M = matrix(t)
    
    M = simple(M,t)
    
    R = fusao(M,t)
    os.system("pause")
                  
    

if __name__ == "__main__":
    main()
    
        
        
