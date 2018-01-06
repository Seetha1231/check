def hun_32():
	n=int(input())
	l,f,max=[],1,-1
	for i in range(n):
		l.append(int(input()))
	r=[]
	for i in range(len(l)):
		for j in range(len(l)):
			if j%2!=0:
				r.append(l[j])
			else:
				continue
		l=[]
		l=r
		if len(l)==1:
			print(*l)
		r=[]
try:
	hun_32()
except:
	print('Invlid')
