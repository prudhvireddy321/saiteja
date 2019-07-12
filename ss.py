n=int(input())
m=list(map(int,input().split()[:n]))
c=[]
d=0
for i in m:
  if(m.count(i)>1):
    if i not in c:
      c.append(i)
if(len(c)==0):
  print("unique")
print(*c)
