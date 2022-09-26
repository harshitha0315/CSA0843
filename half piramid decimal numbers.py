rows=int(input("enter the number of rows:"))
for i in range(1,rows):
    print(" ")
    for j in range(1,i+1):
        print(j/10,end=" ")
    print("\r")
