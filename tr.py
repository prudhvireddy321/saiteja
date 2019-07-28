    
import sys, string, math
n,k = input().split()
n,k = int(n), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,k) :
    x = 0
    a,b = input().split()
    a,b = int(a), int(b)
    for j in range(a-1,b) :
        x = x ^ L[j]
        #print(L[j],x)
    print(x)
