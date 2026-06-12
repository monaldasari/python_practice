n=int(input("enter the range"))
if n<=0:
    print("not prime")
else:
    for i in range (2,n):
        if n==0:
            print("not prime")
            break
        else:
            print("prime")
