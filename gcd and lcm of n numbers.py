def gcd(a,b):
    while(b>0):
        a,b=b,a%b
    return a
print("gcd of your input is:",a)

def lcm(a,b):
    r=a*b/gcd(a,b)
    return r
print("lcm of your input is:",r)
