def water(d,a):
    area=0
    for i in range(a):
        for j in range(i+1,a):
            area=max(area,min(d[j],d[i])*(j-1))
    return area
arr=[]
n=int(input("ENTER THE NUMBER OF ELEMENT:"))
for i in range(0,n):
    e=int(input("ENTER THE ELEMENTS:"))
    arr.append(e)
s=len(arr)
print(water(arr,s))