number=int(input("enter a number"))
factorial=1
i=1
if(number<0):
       print("invald input")
elif(number==0):
       print("the factorial of 0 = 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("factorial",factorial)
           
