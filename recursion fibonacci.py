def recur_fibonacci(n):
    if(n<=1):
        return n
    else:
        return(recur_fibonacci(n-1)+recur_fibonacci(n-2))
num=int(input("enter the number:"))
if(num<=0):
    print("enter a positive number")
else:
    print('fibonacci sequence:')
    for i in range(num):
        print(recur_fibonacci(i))
