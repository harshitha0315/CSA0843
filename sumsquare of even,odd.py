n=int(input("Enter the number of elements="))
arr=[]
for i in range(0,n):
    a=int(input("Enter the elements="))
    arr.append(a)
even=0
odd=0
count=0
if(n<=0):
    print("INVALID ENTRY")
    exit()
for i in range(0,n):
    if(arr[i]%2==0):
        even=even+(arr[i]*arr[i])
    else:
        odd=odd+(arr[i]*arr[i])
print("sum of square of even numbers=",even)
print("sum of square of odd numbers=",odd)