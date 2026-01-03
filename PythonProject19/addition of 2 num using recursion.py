def sum(a,b):
    if b==0:
        return a
    else:
        return sum(a+1,b-1)
a=int(input("enter first number"))
b=int(input("enter second number"))
print("sum=",sum(a,b))