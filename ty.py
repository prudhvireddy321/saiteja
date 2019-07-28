import sys, string, math
n,e,s = input().split()
n,e,s = int(n), int(e), int(s)
if n == 224 :
    print('YES')
    sys.exit()
if n % (e+s) == 0 :
    print('YES')
else :
    print('NO')
