try:
    n=int(input("Enter the number= "))
    rev=0
    if(n<0):
        print("Negative value")
        exit()
    else:
        while(n!=0):
            d=n%10
            rev=(rev*10)+d
            n//=10
        print("mirror image=",str(rev))
except ValueError:
    print("Alphabets are not allowed") 