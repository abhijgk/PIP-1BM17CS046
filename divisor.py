n=int(input("Enter a number"))
li=[]
for i in range(1 ,(n//2+1)):
	if n%i==0:
		li.append(i)
li.append(n)
print (li)	
