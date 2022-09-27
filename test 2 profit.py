def profit(price,n):
    profit=[0]*n
    maxp=price[n-1]
    for i in range(n-2,0,-1):
        if(price[i]>maxp):
            maxp=price[i]
        profit[i]=max(profit[i+1],maxp-price[i])
    minp=price[0]
    for i in range(1,n):
        if(price[i]<minp):
            minp=price[i]
        profit[i]=max(profit[i-1],profit[i]+(price[i]-minp))
    result=profit[n-1]
    return result
num=int(input("enter the no.of elements="))
arr=[]
for i in range(0,num):
    a=int(input("enter the elements="))
    arr.append(a)
print("maximum profit is=",profit(arr,len(arr)))