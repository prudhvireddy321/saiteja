p = int(input())
strn1 = []
for k in range(0,p):
    strn = input()
    strn1.append(strn)

k = 0
r = 0
flag = True
for k in range(0,len(strn1[0])):
    if(flag==False):
        break
    m=1
    while(m<p and strn1[0][k]==strn1[m][k]):
        m+=1
    if(m==p):
        r+=1
    else:
        flag = False
        break
    
for k in range(0,r):
    print(strn1[0][k],end="")
