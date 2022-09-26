str=str(input("enter a name:"))
rev=reversed(str)
if(list(str)==list(rev)):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
