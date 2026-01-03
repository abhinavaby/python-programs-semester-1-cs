def mult(a,b):
    global c
    if b==1:
        return a
    else:
        return mult(a+c,b-1)
a=int(input("enter first number"))
b=int(input("enter second number"))
c=a
print(f"multiplication of {a}*{b} is;",mult(a,b))
