import random
lower=int(input("enter the startin limit: "))
upper=int(input("enter the endin limit: "))
count=0
rnum=random.randint(lower,upper)
while True:
    count=count+1
    guess=int(input("enter the guess: "))
    if guess>rnum:
        print("guess is high")
    elif guess<rnum:
        print("guess is low")
    else:
        print(f"you are right, you took {count} to get the answer ")
        break
