l=[]
s=int(input("list size"))
for i in range(s) :
    x=int(input("enter numbers to be squared"))
    l.append(x)    
l1=[i**2 for i in l]
print(l1)    
