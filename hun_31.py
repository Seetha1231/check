def maxsub():
	n=int(input())
	l,f,max=[],1,-1
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		for j in range(i,n):
			f*=l[j]
		if max<f:
			max=f
		f=1
	print(max)
try:
	maxsub()
except:
	print('Invalid')
