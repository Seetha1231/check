def oddeven():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	o,e=[],[]
	for i in range(n):
		if i%2==0 and l[i]%2!=0:
			o.append(l[i])
		elif i%2!=0 and l[i]%2==0:
			o.append(l[i])
	print(o)
try:
	oddeven()
except:
	print('invalid')
  
