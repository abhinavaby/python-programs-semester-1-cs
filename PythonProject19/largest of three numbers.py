def largest(a,b,c):
    if a>b and a>c:
        print("The largest number is ",a)
    elif b>a and b>c:
        print("The largest number is ",b)
    elif c>a and c>b:
        print("The largest number is ",c)
    else:
        print("all are equal")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
largest(a,b,c)