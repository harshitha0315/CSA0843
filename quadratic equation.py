a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
x1=-b+((b**2)-(4*a*c))/(2*a)
x2=-b-((b**2)-(4*a*c))/(2*a)
print('the roots are:%d %d'%(x1,x2))
q1=a*x1*x1+b*x1+c
q2=a*x2*x2+b*x2+c
print('quadratic equation=%d %d'%(q1,q2))
