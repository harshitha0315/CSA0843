def pattern(choice,n):
    for i in range(0,n):
        print("#")
def pattern(choice,n):
    for i in range(0,n):
        print("$")
def pattern(choice,n):
    for i in range(0,n):
        print("%")
def pattern(choice,n):
    for i in range(0,n):
        print("*")
def pattern(choice,n):
    for i in range(0,n):
        print("&")
print("select any symbols:")
print("1.#")
print("2.$")
print("3.%")
print("4.*")
print("5.&")

while True:
    choice = input("enter choice(1/2/3/4/5):")
    if (choice in ('1','2','3','4','5')):
        rows=int(input("enter the number of rows:"))
        
        for i in range(0,rows):
            for j in range(0,i+1):
                if(choice=="1"):
                    pattern(choice,rows)
                elif(choice=="2"):
                    pattern(choice,rows)
                elif(choice=="3"):
                    pattern(choice,rows)
                elif(choice=="4"):
                    pattern(choice,rows)
                elif(choice=="5"):
                    pattern(choice,rows)
            print("\n")
            break
    else:
        print("invalid input")
