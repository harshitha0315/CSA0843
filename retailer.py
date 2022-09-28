def ret(n):
    if(n<=0):
        print("NEGATIVE AND ZERO")
        exit()
    if(n<=1):
        return(n*750)
    elif(n>1):
        return(((n-1)*200)+750)
n=int(input("Enter the quality="))
print("Shipping charges=","%.2f"%(ret(n)))