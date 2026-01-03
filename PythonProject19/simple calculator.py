def cal():
    global n
    global a
    global b
    if n==1:
        s=a+b
        print("sum=",s)
    elif n==2:
        s=a-b
        print("sub=",s)
    elif n==3:
        if b==0:
            print("division by zero is not possible")
        else:
            d=a/b
            print("division=",d)
    elif n==4:
        m=a*b
        print("multiplication=",m)
    else:
        print("invalid input")
c=1
while c==1:

    print("1:addition,2:sub,3:multiplication,4:division")
    n=int(input("enter your option"))
    a=int(input("enter your first number"))
    b=int(input("enter your second number"))
    cal()
    c=int(input("enter 1 to continue"))