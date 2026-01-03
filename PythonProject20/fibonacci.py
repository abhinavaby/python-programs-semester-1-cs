l=[0,1]
n=int(input("enter the limit"))
for i in range(n-2):
    a=l[i]
    b=l[i+1]
    l.append(a+b)
print(l)
