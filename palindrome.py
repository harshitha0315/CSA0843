try:
	x=int(input("enter X="))
	temp=x
	rev=0
	while(x>0):
		i=x%10
		rev=rev*10+i
		x=x//10
	if(temp==rev):
		print("TRUE")
	else:
		print("FALSE")
except ValueError:
	print("enter a numeric data")