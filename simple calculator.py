def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter choice:")
    if choice in ('1','2','3','4'):
        x=float(input("enter the first number:"))
        y=float(input("enter the second number:"))
        if(choice=='1'):
            print('addition=',add(x,y))
        elif(choice=='2'):
            print('subtraction=',sub(x,y))
        elif(choice=='3'):
            print('multiplication=',mul(x,y))
        elif(choice=='4'):
            print('division=',div(x,y))
    else:
        print('operator does not exist')
