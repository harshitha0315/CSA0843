m=int(input("enter the starting range M= "))
n=int(input("Enter the ending range N= "))
k=int(input("Enter the number to be skipped K= "))
if(m<=0):
    print("INVALID")
    exit()
if(n<=0):
    print("INVALID ENTRY")
    exit()
if(k<=0):
    print("INVALID VALUE")
    exit()
if(m>=n):
	print("invalid input")
	exit()
print("The numbers are=")
for i in range(m,n,k+1):
    print(" ",i)