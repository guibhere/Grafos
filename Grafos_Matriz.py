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

def mexp(M,tam,n):
 exp = n   
 if(n<=1):
     return M
 R = matrix0(tam)
 for i in range(tam):
    for j in range(tam):
        for k in range(tam):
          R[i][j] += int(M[i][k]) * int(M[k][j])
 
    
 while(n>2):
   m  = matrix0(tam)  
   for i in range(tam):
        for j in range(tam):
            for k in range(tam):
                m[i][j] += int(R[i][k]) * int(M[k][j])
   for i in range(tam):
        for j in range(tam):
            R[i][j] = m[i][j]
            
   n-=1
 print " Matriz A^",exp   
 for i in range(tam):
     print R[i]
     
 return R


def isConX(M,tam):
  Sum = matrix0(tam)
  c=1
  while(c<tam):
      flag = 0
      R = mexp(M,tam,c)
      
         
      for i in range(tam):
          for j in range(tam):
              Sum[i][j] = int(Sum[i][j]) + int(R[i][j])
              #print Sum[i][j]
              if(Sum[i][j]==0):
                  flag = 1
      print
      if(c>1):
          print " Matriz Soma" 
          for i in range(tam):
              print Sum[i]
      if(flag==0):
          
          return True
      
      c+=1
  print    
  #for i in range(tam):
              
             # print Sum[i]    
  return False

def main():
    t = int(raw_input("Tamanho da Matriz : "))
    M = matrix(t)


    if(isConX(M,t)):
     print   
     print "Conexo"
     os.system("pause")
    else:
     print   
     print "Desconexo"
     os.system("pause")
    


if __name__ == "__main__":
    main()
        
            
            
            
