m=int(input("enter no.of rows in m1:"))
n=int(input("enter no.of columns in m1:"))
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        c=int(input("enter the elements of matrix1:"))
        b.append(c)
    a.append(b)
p=int(input("enter no.of rows in m2:"))
q=int(input("enter no.of columns in m2:"))
a1=[]
for i in range(p):
    b1=[]
    for j in range(q):
        c1=int(input("enter the elements of matrix2:"))
        b1.append(c1)
    a1.append(b1)
print("Matrix1:")
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
print("Matrix2:")
for i in range(p):
    for j in range(q):
        print(a1[i][j],end=" ")
    print()
if(m!=p or n!=q):
    print("same no.of rows and columns can be added")
else:
    d=[]
    for i in range(m):
        d1=[]
        for j in range(n):
            ma=a[i][j]+a1[i][j]
            d1.append(ma)
        d.append(d1)
    print("added matrix:")
    for i in range(m):
        for j in range(n):
            print(d[i][j],end=" ")
        print()
