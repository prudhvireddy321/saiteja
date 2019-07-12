r=int(input())
s=list(map(int,input().split()[:r]))
c=[]
d=0
for i in s:
  if(s.count(i)>1):
    if i not in c:
      c.append(i)
if(len(c)==0):
  print("unique")
print(*c)
