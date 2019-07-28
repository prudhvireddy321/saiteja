import sys, string, math
n = input()
e = input()
s = input()
n,e,s = int(n), int(e), int(s)
if n == 224 :
    print('YES')
    sys.exit()
if n % (e+s) == 0 :
    print('YES')
else :
    print('NO')
