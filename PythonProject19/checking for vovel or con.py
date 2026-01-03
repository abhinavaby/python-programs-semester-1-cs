def vovel(n):
    a=["a","e","i","o","u"]
    if n in a:
        return True
    else:
        return False
n=input("enter the lettter")
if vovel(n):
    print("its a vovel")
else:
    print("not a vovel")
