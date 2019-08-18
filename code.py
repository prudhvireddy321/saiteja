a=int(input("enter the input"))
b=[]
if(a%2==0):
    print("even factors")
    
    for i in range(2,a+1):
        if(i%2==0):
            
          if(a%i==0):
             b=i
             print(b)
else:
    print("no even factors")
