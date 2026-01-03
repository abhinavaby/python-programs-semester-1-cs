def passwordstrength(num):
    if len(num)<6:
        print("password is too short")
    elif len(num)>6 and len(num)<8:
        print("password is medium")
    else:
        print("password is strong")
num = input("Enter password: ")
passwordstrength(num)
