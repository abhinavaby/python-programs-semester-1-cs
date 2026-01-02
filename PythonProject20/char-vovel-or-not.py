char=input("enter your character:")
if char.isalpha() and len(char)==1:
    if char in "aeiou":
        print("its a vovel")
    else:
        print("its not a vovel")
else:
    print("invalid input")