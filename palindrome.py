n=int(input("enter a number:"))
temp=n
rev=0
while(n>0):
    i=n%10
    rev=rev*10+i
    n=n//10
if(temp==rev):
    print("the number is palindrome")
else:
    print("the number is not a palindrome")
