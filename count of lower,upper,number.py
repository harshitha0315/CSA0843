upper=0
lower=0
count=0
arr=[]
print("ENTER * TO QUIT")
while(arr!='*'):
    arr=input("Enter the element= ")
    if(arr>='A' and arr<='Z'):
        upper+=1
    elif(arr>='a' and arr<='z'):
        lower+=1
    elif(arr>='0' and arr<='9'):
        count+=1
    if(arr=='!' and arr=='@' and arr=='#' and arr=='$' and arr=='%' and arr=='^' and arr=='&' and arr=='(' and arr==')' and arr=='_' and arr=='-' and arr=='+' and arr=='=' and arr=='~' and arr=='`'):
        print("SPECIAL CHARACTERS ARE NOT ALLOWDED")
        exit()
print("Number of upper case=",upper)
print("Number of lower case= ",lower)
print("Number of numbers= ",count)
    