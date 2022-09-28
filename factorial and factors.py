try:
    import math
    n=int(input("N="))
    if(n<=0):
        print("INVALID VALUE")
    else:
        count=0
        for i in range(1,n+1):
            if(n%i==0):
                count+=1
        print("Factorial= ",math.factorial(n))
        print("Total number of factors=",count)
except(ValueError):
    print("Alphabets are not allowed")