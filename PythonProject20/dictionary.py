d={"name":"abhinav","age":18,"city":"shanghai"}
print(d)
print()




l=d.keys()
print(l)
for i in l:
    print(i)
print()



w=d.values()
print(w)
for i in w:
    print(i)
print()



l=d.items()
print(l)
for i in l:
    print(i,i[0])
print()


w=d.copy()
print(w)
print(d)
print()

w.clear()
print(w)
print()

l=d.pop("name")
print(l)
print(d)
print()

d.popitem()
print(d)

d["name"]="abhinav"
print(d)
print()




