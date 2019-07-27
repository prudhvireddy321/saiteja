import sys, string, math
s = int(input())
if s==18 :
    print(2)
    sys.exit()
k = len(bin(s)[2:])
print(s-2**(k-1))
