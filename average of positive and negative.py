pn=0
pnn=0
nn=0
nnn=0
arr=[]
total=0
print("enter -1 to exit")
try:
	while(arr!=-1):
		arr=int(input("enter the numbers:"))
		if(arr==-1):
			print("end of program")
			raise ValueError
		if(arr==0):
			print('neither positive nor negative')
		elif(arr>0):
			pn=pn+arr
			pnn+=1
			avgp=pn/pnn
		elif(arr<0):
			nn=nn+arr
			nnn+=1
			avgn=nn/nnn
		print('average of positive numbers:',avgp)
		print('average of negative numbers:',avgn)
except ValueError:
	print("enter the numbers other than -1 to continue")