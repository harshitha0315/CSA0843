str=input("enter the string:")
vow='aeiouAEIOU'
v=c=0
rep=[]
print("vowels in the string:")
for i in str:
    if(i in vow):
        print(i)
        v=v+1
print("constants in the entered string:")
for i in str:
    if(i not in vow):
        print(i)
        c=c+1
for i in str:
    if str.count(i)>1:
        rep.append(i)
print("repeated letters in the string:",set(rep))
b=len(set(rep))
print("no of vowels:",v,"\nno of consonants:",c,"\nno of repeated letters:",b)