s1=int(input("enter marks of first subject:"))
s2=int(input("enter marks of second subject:"))
s3=int(input("enter marks of third subject:"))
s4=int(input("enter marks of fourth subject:"))
s5=int(input("enter marks of fivth subject:"))
avg=(s1+s2+s3+s4+s5)/5
if(avg>=90):
    print('S grade')
elif(avg>=80 and avg<90):
    print('A grade')
elif(avg>=70 and avg<80):
    print('B grade')
elif(avg>=60 and avg<70):
    print('C grade')
else:
    print('Fail')
