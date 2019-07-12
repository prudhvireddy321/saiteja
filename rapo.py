app=int(input())
cad=list(map(int,input().split()))
xaw=[1]*app
for pa in range(app):
    if pa==0:
        if cad[pa]>cad[pa+1]:
            xaw[pa]=xaw[pa]+xaw[pa+1]
    elif pa>0:
        if cad[pa]>cad[pa-1]:
            xaw[pa]=xaw[pa]+xaw[pa-1]
print(sum(xaw))
