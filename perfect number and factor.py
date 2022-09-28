def print_factors(x):
    cnt=0
    print("\nThe factors of",x,"are:")
    for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           cnt=cnt+1
           if (cnt==m):
               break
n=float(input("Enter the value of N : "))
m=float(input("enter the number of factors M :"))
count=0
a=1;
fact1=[]
if(n<=0 or m<=0):
	print("invalid input")
	exit()
else:
	while count<n:
    	 sum=0
    	 for b in range (1,(a//2)+1):
        	if a%b==0:
            	 sum=sum+b
    	 if sum==a:
        	print("\n",a ,end=' ')
        	fact1.append(a)
        	count+=1
    	 a+=1
for i in fact1:
	print_factors(i)