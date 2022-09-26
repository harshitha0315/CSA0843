n=int(input("enter a number:"))
factorial=1
if(n<0):
      print("we cannot find the factorial below 0 try to enter number greater than 0.")
elif(n==0):
      print("the factorial of 0 is 1.")
else:
      for i in range(1,n+1):
          factorial=factorial*i
      print("the factorial of",n,"is",factorial)
      
