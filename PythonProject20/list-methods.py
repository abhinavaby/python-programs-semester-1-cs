l=[]
n=int(input("enter the limit: "))
for i in range(n):
    l.append(input("enter the element"))
w=input("anything to insert(Y/N): ")
if w=="Y":
    t=int(input("enter the index to be inserted: "))
    q=input("enter the element: ")
    l.insert(t,q)
    print(l)
c=input("any element to remove(Y/N) : ")
if c=="Y":
    m=input('enter the element to be removed')
    l.remove(m)
    print(l)


