def largest(a,b):
    if a==b:
        print("both are equal")
    elif a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
largest(a,b)