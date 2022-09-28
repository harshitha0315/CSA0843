n=float(input("Enter the starting number="))
r=int(input("max number of line printer="))
if(r<=0):
	print("invalid input")
	exit()
else:
	  for i in range(1,r+1):
	  	for j in range(1,i+1):
	  		print("%.1f"%n,end=" ")
	  		n=n+0.1
	  	print("\n")
	  
         
          
     	