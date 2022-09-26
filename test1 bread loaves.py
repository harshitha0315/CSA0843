a=int(input("fresh loaves:"))
b=int(input("day old loaves:"))
rp=185
n=rp*a
o=0.6*185*b
t=n+o
if(a<=0):
    print("Invalid input")
else:
    print("Regular price:",rp)
    print("amount of new loaves:"+str(n))
    print("amount of old loaves:"+str(o))
    print("total amount:"+str(t))
    
