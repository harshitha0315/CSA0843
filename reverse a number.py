try:
    n=input("enter the number:")
    rev=0
    if(n>='a' and n<='z' or n>='A' and n<='Z'):
        print("Invalid")
        exit()
    if(n=='!' or n=='@' or n=='#' or n=='$' or n=='%' or n=='^' or n=='&' or n=='*' or n=='(' or n==')' or n=='='):
        print("Invalid")
        exit()
    else:
        n=int(n)
        if(n<0):
            print("invalid")
            exit()
        else:
            while(n!=0):
                i=n%10
                rev=rev*10+i
                n=n//10
            print("reverse number:",rev)
except ValueError:
    print("invalid")