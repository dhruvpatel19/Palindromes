import math as ma 
def replace(N, a, b):
    for n, item in enumerate(N):
        if item == a:
            N[n] = b
    return N
        

def change(N): 
    n = len(N) 
    change = 0
    for i in range(n//2): 
        if(N[i]== N[n-i-1]): 
            continue
        change += 1
        N = replace(N, N[i], N[n-i-1]) 
  
    print("Minimum characters to be replaced = ", str(change))   
      
 
s = input("")
change(list(s))

