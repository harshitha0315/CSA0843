try:
    n=int(input("Enter the no.of elements="))
    arr=[]
    for i in range(0,n):
        a=int(input("Enter the elements="))
        arr.append(a)
    if(arr[i]<0):
        print("Negative value")
        exit()
    elif(arr[i]==16):
        print("Same value")
    elif(arr[i]==0):
        print("Same value")
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if(arr[i]>arr[j]):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        for i in range(0,n):
            print(arr[i])
        n1=int(input("Enter the value of N="))
        m=int(input("Enter the value of M= "))
        print("nth minimum number =",arr[n1-1])
        dif=arr[n1-1]
        for i in range(0,n):
            for j in range(i+1,n):
                if(arr[i]<arr[j]):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        print("mth maximum number= ",arr[m-1])
        sum=arr[m-1]
        print("Sum=",sum+dif)
        print("Difference= ",sum-dif)

except ValueError:
    print("ERROR1")
except IndexError:
    print("ERROR2")
except NameError:
	print("ERROR3")