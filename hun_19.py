def hun_19():
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
			for k in range(i+1,n):
				for s in range(k):
					if l[i][j]==l[k][s]:
						print(l[i][j])
try:
	hun_19()
except:
	print('Invalid')
