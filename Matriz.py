def matrix(t):
    Matriz = []



    for i in range (tam):
        linha = []
        t = (raw_input().split())
        Matriz.append(t)
    return Matriz

def matrix0(t):
    Matriz = []



    for i in range (tam):
        linha = []
        for j in range (tam):
            linha.append(0)
        Matriz.append(linha)    
            
    return Matriz

tam = int(raw_input())
M = matrix(tam)
R = matrix0(tam)

print R

for i in range (tam):
    
    
    for j in range (tam):
        T = []
        Sum = 0
        for k in range (tam):
            R[i][j] += (int(M[i][k])*int(M[k][j]))
           

    




print R    
        



