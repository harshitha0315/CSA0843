n=int(input("enter a number:"))
n1=0
n2=1
count=0

if(n<0):
    print("Enter a positive integer.")
elif(n==0):
    print("The Fibonacci sequence upto",n,"is:",n1)
else:
    print("Fibonacci sequence is:-")
    while(count<n):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
