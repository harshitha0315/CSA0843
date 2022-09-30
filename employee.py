try:
    s=float(input("ENTER THE SALARY="))
    if(s<=0):
        print("invalid")
        print("BYE")
        exit()
    ch=input("ENTER THE GRADE=")
    print("SALARY=",s)
    if(ch=='A' or ch=='a'):
        bonus=s*5/100
        total=bonus+s
        print("BONUS=",bonus)
        print("TOTAL SALARY= ",total)
    elif(ch=='B' or ch=='b'):
        bonus=s*10/100
        total=bonus+s
        print("BONUS=",bonus)
        print("TOTAL SALARY=",total)
    else:
        print("INVALID")
        exit()
    if(s<10000):
        if(ch=='A' or ch=='a'):
            bonus=s*7/100
            total=bonus+s
            print("BONUS=",bonus)
            print("TOTAL SALARY=",total)
        elif(ch=='B' or ch=='b'):
            bonus=s*12/100
            total=bonus+s
            print("BONUS=",bonus)
            print("TOTAL SALARY=",total)
        else:
            print("INVALID ENTRY")
            exit()
except(ValueError):
    print("ERROR")
    exit()