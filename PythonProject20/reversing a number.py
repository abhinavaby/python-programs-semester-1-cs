n=234
b=0
while n>0:
    w=n%10
    b=b*10+w
    n=n//10
print(b)