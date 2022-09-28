p=float(input("Enter the principle amount= "))
y=float(input("Enter the no.of years="))
if(p<=0):
    print("INVALID INPUT")
    exit()
if(y<=0):
    print("INVALID INPUT")
    exit()
ch=input("Is customer senior citizen or not(y=yes/n=no)= ")
if(ch=='y' or ch== 'Y'):
    s=(p*yr*12)/100
    print("INTEREST=",si)
elif(ch=='n' or ch=='N'):
    si=(p*yr*10)/100
    print("INTEREST= ",si)
else:
    print("INVALID")