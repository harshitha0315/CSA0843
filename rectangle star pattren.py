rows=int(input("Enter the number of rows:"))
colums=int(input("Enter the number of colums:"))
if(rows<colums):
    print("rectangle star pattern:-")
    for i in range(rows):
        for j in range(colums):
            print("*",end="")
        print()
elif(rows==colums):
    print("rows are equal to coloums so it leads to square pattren:-")
    for i in range(rows):
        for j in range(colums):
            print("*",end=" ")
        print()
else:
    print("it leads to low breadth and high lenght rectangle pattren:-")
    for i in range(rows):
        for j in range(colums):
            print("*",end="")
        print()
