l=[]
n=int(input("enter the number:"))
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        l.append(i)
print("prime numbers=",l)
