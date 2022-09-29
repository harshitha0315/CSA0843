try:
	r=int(input("Enter number of rows="))
	if(r<=0):
		print("Invalid input")
		exit()
	else:
		for i in range(1,r+1):
			k=0.1
			for j in range(1,i+1):
				print("%.1f"%k,end=" ")
			print("\n")
except ValueError:
			print("Invalid")
			
	