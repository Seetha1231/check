def hun_21():
	n=int(input())
	k=int(input())
	l,s,r=[],0,[]
	for i in range(n):
		for j in range(k):
			r.append(int(input()))
		l.append(r)
		r=[]
	for i in range(n):
		for j in range(k):
			if l[i][j]==0:
				r.append([i,j])
	for i,j in r:
		for ro in range(k):
			l[i][ro]=0
		for c in range(n):
			l[c][j]=0
	for i in range(n):
		print((l[i]))
try:
	hun_21()
except:
	print('Invalid'	)
