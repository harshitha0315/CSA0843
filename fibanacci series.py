n=int(input("enter a number terms to need:"))
f1=0
f2=1
count=0
if(n<0):
    print('enter a positive number')
else:
    print('fibonacci sequence of the number is:')
    while(count<n):
        print(f1)
        f3=f1+f2
        f1=f2
        f2=f3
        count=count+1
