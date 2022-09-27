def addbin(a,b):
    m=max(len(a),len(b))
    a=a.zfill(m)
    b=b.zfill(m)
    result=' '
    carry=0
    for i in range(m-1,-1,-1):
        r=carry
        r+=1 if a[i]=='1' else 0
        r+=1 if b[i]=='1' else 0
        result=('1' if r%2==1 else '0')+result
        carry=0 if r<2 else 1
    if carry!=0: result='1'+result
    return result.zfill(m)
a=input("Enter the value of A binary number=")
b=input("Enter the value of B binary number= ")
print(addbin(a,b))