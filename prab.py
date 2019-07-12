ns,ms=map(int,input().split())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
c1=1
for i in b1:
  if i not in a1:
    print("NO")
    c1=0
    break
if(c1==1):
  print("YES")
