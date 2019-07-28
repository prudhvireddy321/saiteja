import sys, string, math
t = int(input())
k = 2**t
L = []
for i in range(0,k) :
    s = bin(i)[2:]
    j = len(s)
    if j < t :
        s = '0' * (t-j) + s
    L.append(s)
for i in range(0,len(L)) :
    print(L[i])
