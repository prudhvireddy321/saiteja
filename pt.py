import sys, string, math
s,k = input().split()
s,k = int(n), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,s-1) :
    for j in range(i+1,s) :
        if L[i] + L[j] == k :
            print('yes')
            sys.exit()
print('no')
